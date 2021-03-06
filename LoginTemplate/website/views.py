from flask import Blueprint, current_app, jsonify, redirect, render_template, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from . import db


# import json
views = Blueprint('views', __name__)


@views.route('/<uname>', methods=['GET', 'POST'])
@login_required
def home(uname):
    print(current_user)
    if uname == '':
        uname='undefined'
    return render_template( 'home.html' , uname = uname )

