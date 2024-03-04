from flask import Blueprint, render_template, session, request
from src.utils.jwt import generate_jwt

home = Blueprint('home', __name__)

@home.route('/')
def homePage():
    return '<h1>welcome to api in flask</h1>'
