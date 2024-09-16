"""
    Configuration class for the application.
"""

import os

from dotenv import load_dotenv

load_dotenv()


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
