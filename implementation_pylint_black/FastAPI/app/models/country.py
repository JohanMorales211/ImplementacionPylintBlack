"""
This module contains the Country and City models.
"""

from pydantic import BaseModel

class Country(BaseModel):
    """
    Country model representing a country with an id, name, and continent.
    """
    id: int
    name: str
    continent: str

class City(BaseModel):
    """
    City model representing a city with an id, name, population, and country_id.
    """
    id: int
    name: str
    population: int
    country_id: int
