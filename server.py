#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Matt Martz
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import base64
import json
import os

import docker

from flask_lambda import FlaskLambda
from flask import request, jsonify


kwargs = {}
app_path = os.path.dirname(__file__)
kwargs.update({
    'static_url_path': '',
    'static_folder': os.path.join(os.path.abspath(app_path),
                                  'client')
})

app = FlaskLambda(__name__, **kwargs)
@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/render', methods=['POST'])
def render_template():
    data = request.get_json()

    client = docker.from_env()
    try:
        stdout = client.containers.run(
            "ansible-template-ui",
            environment={
                'TEMPLATE': base64.b64encode(data['template']),
                'VARIABLES': base64.b64encode(data['variables'] or '{}')
            },
            stdout=True,
            stderr=False,
            detach=False,
            remove=True,
            mem_limit='96m',
        )
    except Exception as e:
        return jsonify(**{'error': e.stderr}), 400

    try:
        data = json.loads(stdout)
    except Exception as e:
        print stdout
        return jsonify(**{'error': str(e)}), 400

    content = data['plays'][0]['tasks'][1]['hosts']['localhost']['content']
    return jsonify(**{'content': base64.b64decode(content)})


if __name__ == '__main__':
    app.run(debug=True)
