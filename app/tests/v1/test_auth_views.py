#!/usr/bin/env python3
""" Tests Authentication routes """
import unittest
import json
from app import create_app


class TestSignupRoute(unittest.TestCase):
    """ Test case for the signup authentication blueprint """
    def setUp(self):
        """ Test Variables """
        self.app = create_app(config_mode="testing")
        self.client = self.app.test_client
        self.good_reg_data = {
            "username": "shelockholmes",
            "email": "consultingdetective@email.com",
            "password": "scienceofdeduction",
            "firstname": "Sherlock",
            "lastname": "Holmes",
            "confirm password": "scienceofdeduction",

        }

    def test_signup_with_valid_input(self):
        """ Test that valid signup user data gets registered succesfully """
        response = self.client().post("/signup", data=self.good_reg_data)
        deserialized_response = json.loads(response.data.decode())
        self.assertEqual(
            response.status_code, 201,
            msg="response code SHOULD BE 201 (Created)"
        )
        self.assertEqual(
            deserialized_response["message"],
            "Successfully Registered. Please login.",
            msg="Response Body Contents- Should be success msg to user"
        )

    def test_signup_with_an_existing_username(self):
        """ Tests hanlding of an already existing username """
        response = self.client().post("/signup", data=self.good_reg_data)
        self.assertEqual(
            response.status_code,
            201,
            msg="response code SHOULD BE 201 (Created)"
        )
        # Try registering the same user again
        sec_response = self.client().post("/signup", data=self.good_reg_data)
        self.assertEqual(
            sec_response.status_code,
            202,
            msg="response code SHOULD BE 202 (Accepted)"
        )
        # JSON-Pyton Object - User already exists. Please login.
        deserialized_sec_resp = json.loads(sec_response.data.decode())
        self.assertEqual(
            deserialized_sec_resp["message"],
            "Username already exists. Please login.",
            msg="response data should custom message to user"
        )

    def test_with_wrong_key_value_pairs(self):
        """ Test payload contains only the expected key value pairs """
        malformed_reg_data = {
            "usernames": "shelockholmes",
            "emails": "consultingdetective@email.com",
            "passwords": "scienceofdeduction",
            "firstnames": "Sherlock",
            "lastnames": "Holmes",
            "confirm passwords": "scienceofdeduction",

        }
        response = self.client().post("/signup", data=malformed_reg_data)
        self.assertEqual(
            response.status_code,
            400,
            msg="Bad Request - Malformed payload"
        )
        deserialized_resp = json.loads(response.data.decode())
        self.assertEqual(
            deserialized_resp["message"],
            "Invalid key value pairs in payload",
            msg="Bad Request - Malformed payload"
        )

    def test_with_blank_fields_in_payload(self):
        """ Tests that the user input fields cannot be blank """
        blank_reg_data = {
            "username": "",
            "email": "consultingdetective@email.com",
            "password": "scienceofdeduction",
            "firstname": "Sherlock",
            "lastname": "Holmes",
            "confirm password": "scienceofdeduction",

        }
        response = self.client().post("/signup", data=blank_reg_data)
        self.assertEqual(
            response.status_code,
            202,
            msg="response code SHOULD BE 202 (Accepted)"
        )
        deserialized_resp = json.loads(response.data.decode())
        self.assertEqual(
            deserialized_resp["message"],
            "Input fields cannot be blank. Please try again.",
            msg="response data should custom message to user"
        )

    def test_with_existng_email(self):
        """ Test that the provided email is not already registered
            with another account
        """
        reg_data_existing_email = {
            "username": "drwatson",
            "email": "consultingdetective@email.com",
            "password": "readmyblog",
            "firstname": "John",
            "lastname": "Watson",
            "confirm password": "scienceofdeduction",

        }
        response = self.client().post("/signup", data=reg_data_existing_email)
        self.assertEqual(
            response.status_code,
            202,
            msg="response code SHOULD BE 202 (Accepted)"
        )
        deserialized_resp = json.loads(response.data.decode())
        self.assertEqual(
            deserialized_resp["message"],
            "The email provided is already registered with another user.",
            msg="response data should custom message to user"
        )

    def test_with_invalid_email_syntax(self):
        """ Tests that the email is syntactically valid """
        invalid_email_reg_data = {
            "username": "mycroft",
            "email": "consulting@detective@emailcom",
            "password": "scienceofdeduction",
            "firstname": "Sherlock",
            "lastname": "Holmes",
            "confirm password": "scienceofdeduction",

        }
        response = self.client().post("/signup", data=invalid_email_reg_data)
        self.assertEqual(
            response.status_code,
            202,
            msg="response code SHOULD BE 202 (Accepted)"
        )
        deserialized_resp = json.loads(response.data.decode())
        self.assertEqual(
            deserialized_resp["message"],
            "Invalid email. Please confirm syntax and try again",
            msg="response data should custom message to user"
        )

    def test_with_invalid_password_length(self):
        """ Tests that the password is atleast 6 characters long """
        invalid_email_reg_data = {
            "username": "mycroft",
            "email": "mycroftholmes@email.com",
            "password": "short",
            "firstname": "Sherlock",
            "lastname": "Holmes",
            "confirm password": "short",
        }
        response = self.client().post("/signup", data=invalid_email_reg_data)
        self.assertEqual(
            response.status_code,
            202,
            msg="response code SHOULD BE 202 (Accepted)"
        )
        deserialized_resp = json.loads(response.data.decode())
        self.assertEqual(
            deserialized_resp["message"],
            "Invalid password. (minimum of 6 characters)",
            msg="response data should custom message to user"
        )

    def test_with_mismatched_password(self):
        """ Tests that the user password and confimation password match """
        invalid_passwords_reg_data = {
            "username": "mycroft",
            "email": "consultingdetective@email.com",
            "password": "scienceofdeduction",
            "firstname": "Sherlock",
            "lastname": "Holmes",
            "confirm password": "sciencesofdeduction",
        }
        response = self.client().post(
            "/signup", data=invalid_passwords_reg_data
        )
        self.assertEqual(
            response.status_code,
            202,
            msg="response code SHOULD BE 202 (Accepted)"
        )
        deserialized_resp = json.loads(response.data.decode())
        self.assertEqual(
            deserialized_resp["message"],
            "Passwords do not match. Please try again",
            msg="response data should custom message to user"
        )


if __name__ == "__main__":
    unittest.main()
