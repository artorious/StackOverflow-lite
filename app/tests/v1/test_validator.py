#!/usr/bin/env python3
""" Input validator """
import unittest
from app.api.v1.validator import (
    check_for_any_empty_fields,
    check_valid_email_syntax,
    check_valid_password_length,
    check_confirmation_password_matches
)


class TestForEmptyFields(unittest.TestCase):
    """ Test cases to Check for empty fields """
    def test_with_valid_data(self):
        """ Test that input string is not empty """
        reg_data = {
            "username": "artorious",
            "email": "consultingdetective@email.com",
            "password": "scienceofdeduction",
            "firstname": "Sherlock",
            "lastname": "Holmes",
            "confirm password": "scienceofdeduction"
        }
        self.assertIs(
            check_for_any_empty_fields(reg_data),
            True,
            msg="Valid registration Data."
        )

    def test_with_empty_username(self):
        """ Test that input string is not empty """
        blank_username = {
            "username": "",
            "email": "consultingdetective@email.com",
            "password": "scienceofdeduction",
            "firstname": "Sherlock",
            "lastname": "Holmes",
            "confirm password": "scienceofdeduction"
        }
        self.assertIs(
            check_for_any_empty_fields(blank_username),
            False,
            msg="Input fields cannot be blank."
        )

    def test_with_empty_password(self):
        """ Test that input string is not empty """
        blank_email = {
            "username": "artorious",
            "email": "consultingdetective@email.com",
            "password": "scienceofdeduction",
            "firstname": "Sherlock",
            "lastname": "Holmes",
            "confirm password": "         "
        }
        self.assertIs(
            check_for_any_empty_fields(blank_email),
            False,
            msg="Input fields cannot be blank."
        )


class TestForEmailSyntax(unittest.TestCase):
    """ Test cases to check for email syntax """
    def test_with_valid_email(self):
        """ Test that email syntax is valid"""
        self.assertIs(
            check_valid_email_syntax("consultingdetective@email.com"),
            True,
            msg="Input fields cannot be blank."
        )

    def test_with_invalid_email(self):
        """ Test that email syntax is valid """
        self.assertIs(
            check_valid_email_syntax("consultingdetectiveemail.com"),
            False,
            msg="Invalid email address syntax"
        )
        self.assertIs(
            check_valid_email_syntax("consultingdetective@emailcom"),
            False,
            msg="Invalid email address syntax"
        )
        self.assertIs(
            check_valid_email_syntax("consultingdetectiveemailcom"),
            False,
            msg="Invalid email address syntax"
        )


class TestForPasswordLength(unittest.TestCase):
    """ Test cases to check for Password length  """
    def test_with_valid_password(self):
        """ Test password is atleast 6 alpha numeric characters """
        self.assertIs(check_valid_password_length("123456"), True)
        self.assertIs(check_valid_password_length("aeiou1"), True)

    def test_with_invalid_password(self):
        """ Test password is atleast 6 alpha numeric characters """
        self.assertIs(check_valid_password_length("1234a"), False)
        self.assertIs(check_valid_password_length("  12345"), False)
        self.assertIs(check_valid_password_length("12345   "), False)
        self.assertIs(check_valid_password_length("\t12345\n"), False)


class TestForPasswordMatching(unittest.TestCase):
    """ Test cases to check password and confirm password match  """
    def test_with_matching_passwords(self):
        """ Test password and confirm password match"""
        self.assertIs(
            check_confirmation_password_matches("123456", "123456"),
            True
        )

    def test_with_mismatched_passwords(self):
        """ Test password and confirm password match"""
        self.assertIs(
            check_confirmation_password_matches("123456", "12345"),
            False
        )
        self.assertIs(
            check_confirmation_password_matches("123456", "0123456"),
            False
        )
        self.assertIs(
            check_confirmation_password_matches("1234560", "123456"),
            False
        )


if __name__ == "__main__":
    unittest.main()
