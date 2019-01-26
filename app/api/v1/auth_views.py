#!/usr/bin/env python3
""" Authentication views/routes - Signup and Login """
from flask import Blueprint

auth_bp_v1 = Blueprint("auth_v1", __name__, url_prefix="/api/v1/auth")

