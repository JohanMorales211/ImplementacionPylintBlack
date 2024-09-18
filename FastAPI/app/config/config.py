# config.py

"""
Configuration class for the application.

This class is responsible for loading and providing configuration settings
for the application. It uses environment variables to set the database
connection details and other sensitive information. If an environment variable
is not set, a default value is used.

Attributes:
    DATABASE_HOST (str): The hostname of the database server.
    DATABASE_PORT (int): The port number of the database server.
    DATABASE_USER (str): The username for the database connection.
    DATABASE_PASSWORD (str): The password for the database connection.
    DATABASE_NAME (str): The name of the database.
    DATABASE_URL (str): The URL for the database connection.
    SECRET_KEY (str): The secret key used for encryption and session management.
    API_KEY (str): The API key used for accessing external services.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# pylint: disable=too-few-public-methods
class Config:
    """
    Configuration class for the application.
    """

    DATABASE_HOST = os.getenv("DATABASE_HOST", "eam_database")
    DATABASE_PORT = int(os.getenv("MYSQL_PORT", "3306"))
    DATABASE_USER = os.getenv("DATABASE_USER", "root")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "root")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "implementation_pylint_black")

    DATABASE_URL = (
        f"mysql+mysqlclient://{DATABASE_USER}:{DATABASE_PASSWORD}"
        f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )

    SECRET_KEY = os.getenv("SECRET_KEY")
    API_KEY = os.getenv("API_KEY")
