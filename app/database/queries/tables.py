from datetime import datetime
from enum import Enum

from pypika import Parameter as CommonParameter
from pypika import Query
from pypika import Table


class Parameter(CommonParameter):
    def __init__(self, count: int) -> None:
        super().__init__(f"${count}")


class TypedTable(Table):
    __table__ = ""

    def __init__(
        self,
        name: str | None = None,
        schema: str | None = None,
        alias: str | None = None,
        query_cls: Query | None = None,
    ) -> None:
        if name is None:
            if self.__table__:
                name = self.__table__
            else:
                name = self.__class__.__name__

        super().__init__(name, schema, alias, query_cls)


class Rating(Enum):
    INAC = -1,
    SUS = 0,
    OBS = 1,
    S1 = 2,
    S2 = 3,
    S3 = 4,
    C1 = 5,
    C2 = 6,
    C3 = 7,
    I1 = 8,
    I2 = 9,
    I3 = 10,
    SUP = 11,
    ADM = 12


class Users(TypedTable):
    __table__ = "users"
    id: int
    first_name: str
    last_name: str
    email: str
    rating: Rating
    created_at: datetime
    updated_at: datetime


users = Users()
