#!/bin/bash
python setup.py sdist
pex -o ansible_template_ui.pex -r deploy-requirements.txt -r pex-requirements.txt -f ./dist -m 'gunicorn.app.wsgiapp:run' --python-shebang='#!/usr/bin/env python'
