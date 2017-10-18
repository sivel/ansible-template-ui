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
