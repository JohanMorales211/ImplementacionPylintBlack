"""
This module establishes a connection to a MySQL database 
using Peewee ORM and environment variables.
"""

import os
from dotenv import load_dotenv
from peewee import MySQLDatabase, Model, AutoField, CharField, ForeignKeyField

# Load environment variables from the .env file
load_dotenv()

# Create a MySQL database instance using environment variables
DATABASE = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

# pylint: disable=too-few-public-methods
class UserModel(Model):
    """Represents a user with attributes such as username, email, and password."""

    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        """Meta information for the UserModel."""

        database = DATABASE
        table_name = "users"


class ProfileModel(Model):
    """Represents a user's profile with attributes such as user_id, profile photo, and biography."""

    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref="profiles")
    profile_photo = CharField(max_length=255)
    biography = CharField(max_length=500)

    class Meta:
        """Meta information for the ProfileModel."""

        database = DATABASE
        table_name = "profiles"
