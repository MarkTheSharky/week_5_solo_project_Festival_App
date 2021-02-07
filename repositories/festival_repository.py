from db.run_sql import run_sql

from models.festival import Festival
from models.country import Country

def save(festival):
    sql = "INSERT INTO festivals (name, country_id) VALUES (%s, %s) RETURNING *"
    values = [festival.name, festival.country.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    festival.id = id
    return festival

# def select_all():
