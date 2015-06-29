# -*-coding:Utf-8 -*-

"""Contains functions that interpret commmands from the CLI and call request functions for user's management"""

import python_compat as pyt_compat
import requests_functions as req


def list():
    """List all users in the database"""
    return req.list()


def search():
    """Search a user according to the pattern"""
    pattern = pyt_compat.input_compat("Pattern: ")
    return req.search({'<pattern>': pattern})


def create():
    """Ask arguments for user creation"""
    email = pyt_compat.input_compat("Email: ")
    sshkey = pyt_compat.input_compat("SSHKey: ")
    comment = pyt_compat.input_compat("Comment: ")

    return req.create(
        {'<email>': email, '<comment>': comment, '<sshkey>': sshkey})


def show():
    """Ask arguments for showing user"""
    email = pyt_compat.input_compat("Email: ")

    return req.show({'<email>': email})


def edit():
    """Ask arguments for editing an existing user"""
    email = pyt_compat.input_compat("Email of the user you want to modify: ")

    if req.show({'<email>': email}) == 0:
        new_email = pyt_compat.input_compat("New email: ")
        new_comment = pyt_compat.input_compat("New comment: ")
        new_sshkey = pyt_compat.input_compat("New SSH key: ")

        return req.edit({'<email>': email,
                         '--newemail': new_email,
                         '--newcomment': new_comment,
                         '--newsshkey': new_sshkey})


def delete():
    """Ask arguments for deleting an existing user"""
    email = pyt_compat.input_compat("Email: ")

    return req.delete({'<email>': email})
