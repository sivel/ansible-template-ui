#!/bin/bash

pex -o ansible_template_ui.pex -r pex-requirements.txt -f ./dist -m 'gunicorn.app.wsgiapp:run'
