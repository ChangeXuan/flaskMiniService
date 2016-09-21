from flask import render_template,redirect, request, url_for, flash , jsonify ,abort
from flask.ext.login import login_user,login_required,logout_user,current_user

from . import main
from .forms import RegistrationForm,LoginForm
from .. import db
from ..models import User

@main.route('/register', methods=['POST'])
def register():
    if not request.form:
        abort(400)
    form = RegistrationForm()
    if User.query.filter_by(email=form.email.data).first():
        return jsonify({"register":"false"})
    user = User(email=form.email.data,
                    username=None,
                    password=form.password.data)
    db.session.add(user)
    db.session.commit()
    return jsonify({"register ":"success"})


@main.route('/login', methods=['POST'])
def login():
    if not request.form:
        abort(400)
    form = LoginForm()
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
        login_user(user,form.remember_me.data)
        return jsonify({"login":"success"})
    else:
        return jsonify({"login":"false"})