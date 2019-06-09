import logging
import flask
from flask import Blueprint
import pycodcif
import os, sys
import json
import random
from flask_paginate import Pagination, get_page_parameter
lib_path = os.path.abspath(os.path.join('..', 'tools-barebone', 'webservice'))
sys.path.append(lib_path)
from run_app import mysql
blueprint = Blueprint('compute', __name__, url_prefix='/compute')

logger = logging.getLogger('tools-app')
users = list(range(45947))


def get_users(offset=0, per_page=50):
    return users[offset: offset + per_page]

@blueprint.route('/database', defaults={'page':1})
@blueprint.route('/database/page/<int:page>')
def database(page):
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    #Create Cursor
    cur = mysql.connection.cursor()
    cur.execute('SELECT ID, URL FROM cif;', (startat,perpage))
    #Close Connection
    cur.close()
    data = list(cur.fetchall())
    return flask.render_template('db.html', users=pagination_users, page=page, per_page=per_page, pagination=pagination, data = data)

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
