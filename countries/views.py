from ninja import Router

from .errors import CountryAlreadyExistsError, CountryNotFoundError
from .schemas import CountryIn, CountryListResponse, CountryOut
from .temporary_db import my_db

countries_router = Router()


@countries_router.get("/", response=CountryListResponse)
def index(request):
    """List all countries"""

    count = len(my_db)
    return {"countries": my_db, "count": count}


@countries_router.get("/{country_id}", response=CountryOut)
def show(request, country_id: int):
    """Show a single country by id"""

    if country_id > len(my_db):
        raise CountryNotFoundError
    return my_db[country_id - 1]


@countries_router.post("/", response=CountryOut)
def create(request, country: CountryIn):
    """Create a new country"""

    country_data = country.model_dump()

    for c_obj in my_db:
        if c_obj["name"] == country_data["name"]:
            raise CountryAlreadyExistsError

    country_data["id"] = len(my_db) + 1
    my_db.append(country_data)

    return CountryOut(**country_data)
