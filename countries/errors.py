from ninja.errors import HttpError
from dataclasses import dataclass


@dataclass
class CountryAlreadyExistsError(HttpError):
    status_code = 400
    message = "Country already exists"


@dataclass
class CountryNotFoundError(HttpError):
    status_code = 404
    message = "Country is not found"
