#!/usr/bin/env python3
""" Authentication views/routes - Signup and Login """
from flask import Blueprint

auth_bp_v1 = Blueprint("auth_v1", __name__, url_prefix="/api/v1/auth")

@auth_bp_v1.route("/signup", methods=["POST"])
def signup():
    """ Register a user - POST """
    # prompt user for data
    # check keys for keys
    # Validate signup data
    # check for user
    # Register user in DB
    # Return custom msg (pass/fail)
    pass