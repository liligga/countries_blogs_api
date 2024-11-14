from ninja import Schema


class CountryOut(Schema):
    id: int
    name: str
    capital: str


class CountryIn(Schema):
    name: str
    capital: str


class CountryListResponse(Schema):
    countries: list[CountryOut]
    count: int
