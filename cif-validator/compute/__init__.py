import logging
import flask
from flask import Blueprint
import pycodcif
import os
import json
import random
blueprint = Blueprint('compute', __name__, url_prefix='/compute')

logger = logging.getLogger('tools-app')


@blueprint.route('/validate/', methods=['GET', 'POST'])
def validate():
    """
    API Route for validation

    Parameters: Accepts a file with key 'cif' via POST
    Function: Validates the file using PyCodCIF
    Response: A JSON Object containing the key 'status' which may hold the values 'valid' or 'error', and the key 'message'.
    """

    if flask.request.method == 'POST':
        # The request method is POST
        file = flask.request.files['cif'] # The file must have the key 'cif'
        filename = ("testfile_" + str(random.randint(1, 1000000)) + ".cif") # Generate Filename
        file.save(filename) # Save the file, PyCodCIF reads only saved files
        response = {'status': '', 'message': []}
        try:
            conf = {}
            for option in flask.request.form.items():
                conf[option[0]] = 1
            data, err_count, err_msg = pycodcif.parse(filename, conf)
            response['status']='valid'
            response['message'].append(err_msg)
        except Exception as e:
            # Pycodcif could not parse the file
            e = str(e).replace("\n", " ")
            error = 'Failed to parse the cif file: ' + e
            response['status']='error'
            response['message'].append(error)
        try:
            # Remove saved file
            os.remove(filename)
        except Exception as e:
            e = str(e).replace("\n", " ")
            response['message'].append(error)
        return json.dumps(response) # Return JSON


@blueprint.route('/')
def index():
    """
    Index Route

    Function: Renders the upload page
    """
    return flask.render_template('upload.html')

