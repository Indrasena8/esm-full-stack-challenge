from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List

from esm_fullstack_challenge.db import DB
from esm_fullstack_challenge.dependencies import get_db
from esm_fullstack_challenge.models import AutoGenModels
from esm_fullstack_challenge.routers.utils import get_route_list_function, get_route_id_function

drivers_router = APIRouter()
Driver = AutoGenModels["drivers"]

class DriverIn(BaseModel):
    driver_ref: str
    number: int | None = None
    code: str | None = None
    forename: str
    surname: str
    dob: str
    nationality: str
    url: str

def row_to_dict(cursor, row):
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}

# ------------- existing GET routes -----------------
get_driver = get_route_id_function('drivers', Driver)
drivers_router.add_api_route(
    '/{id}', get_driver,
    methods=["GET"], response_model=Driver,
)

get_drivers = get_route_list_function('drivers', Driver)
drivers_router.add_api_route(
    '', get_drivers,
    methods=["GET"], response_model=List[Driver],
)

@drivers_router.post("", response_model=Driver, status_code=status.HTTP_201_CREATED)
def create_driver(payload: DriverIn, db: DB = Depends(get_db)):
    cols = ", ".join(payload.dict().keys())
    marks = ", ".join(["?"] * len(payload.dict()))
    values = tuple(payload.dict().values())

    with db.get_connection() as conn:
        cursor = conn.execute(f"INSERT INTO drivers ({cols}) VALUES ({marks})", values)
        new_id = cursor.lastrowid
        cursor = conn.execute("SELECT * FROM drivers WHERE id = ?", (new_id,))
        row = cursor.fetchone()
        driver_dict = row_to_dict(cursor, row)
    return Driver(**driver_dict)

@drivers_router.put("/{id}", response_model=Driver)
def update_driver(id: int, payload: DriverIn, db: DB = Depends(get_db)):
    sets = ", ".join([f"{c}=?" for c in payload.dict().keys()])
    values = tuple(payload.dict().values()) + (id,)

    with db.get_connection() as conn:
        cursor = conn.execute(f"UPDATE drivers SET {sets} WHERE id = ?", values)
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Driver not found")
        cursor = conn.execute("SELECT * FROM drivers WHERE id = ?", (id,))
        row = cursor.fetchone()
        driver_dict = row_to_dict(cursor, row)
    return Driver(**driver_dict)

@drivers_router.delete("/{id}", response_model=Driver)
def delete_driver(id: int, db: DB = Depends(get_db)):
    with db.get_connection() as conn:
        cursor = conn.execute("SELECT * FROM drivers WHERE id = ?", (id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Driver not found")
        driver_dict = row_to_dict(cursor, row)
        conn.execute("DELETE FROM drivers WHERE id = ?", (id,))
    return Driver(**driver_dict)