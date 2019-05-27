import logging
import flask
from flask import Blueprint
import pycodcif
import os
import json
import random
blueprint = Blueprint('compute', __name__, url_prefix='/compute')

logger = logging.getLogger('tools-app')

@blueprint.route('/process_structure/', methods=['GET', 'POST'])
def process_structure():
    if flask.request.method == 'POST':
        structurefile = flask.request.files['structurefile']
        fileformat = flask.request.form.get('fileformat', 'unknown')
        filecontent = structurefile.read().decode('utf-8')

        try:
            return "FORMAT: {}<br>CONTENT:<br><code><pre>{}</pre></code>".format(fileformat, filecontent)
        except Exception:
            flask.flash("Unable to process the data, sorry...")
            return flask.redirect(flask.url_for('input_data'))
    else:
        return flask.redirect(flask.url_for('compute.process_structure_example'))


@blueprint.route('/process_example_structure/', methods=['GET', 'POST'])
def process_structure_example():
    if flask.request.method == 'POST':
        return "This was a POST"
    else:
        return "This was a GET"


@blueprint.route('/validate/', methods=['GET', 'POST'])
def validate():
    if flask.request.method == 'POST':
        file = flask.request.files['cif']
        filename = ("testfile_" + str(random.randint(1, 1000000)) + ".cif")
        file.save(filename)
        try:
            conf = {}
            for option in flask.request.form.items():
                conf[option[0]] = 1
            data, err_count, err_msg = pycodcif.parse(filename, conf)
            data[0]['err_count'] = err_count
            data[0]['err_msg'] = err_msg
        except Exception as e:
            e = str(e).replace("\n", " ")
            error = 'Failed to parse the cif file: ' + e
            data = [{'err_msg': error, }]
        try:
            os.remove(filename)
        except Exception as e:
            e = str(e).replace("\n", " ")
            error = 'Error: ' + e
            data = [{'err_msg': error, }]
        return json.dumps(data)


@blueprint.route('/')
def index():
    return flask.render_template('upload.html')

