#!/usr/bin/env python3
"""
A module for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Function that hashes a password using a random salt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Function that checks if hashed password was formed from given password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
