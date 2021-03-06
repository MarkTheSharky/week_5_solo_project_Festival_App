from db.run_sql import run_sql

from models.festival import Festival
from models.country import Country
import repositories.country_repository as country_repository

def save(festival):
    sql = "INSERT INTO festivals (name, country_id) VALUES (%s, %s) RETURNING *"
    values = [festival.name, festival.country.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    festival.id = id
    return festival

def select_all():
    festivals = []
    sql = "SELECT * FROM festivals"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select_by_id(row['country_id'])
        festival = Festival(row['name'], country, row['id'])
        festivals.append(festival)
    return festivals

def select_by_id(id):
    festival = None
    sql = "SELECT * FROM festivals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select_by_id(result['country_id'])
        festival = Festival(result['name'], country, result['id'])
    return festival

def delete_all():
    sql = "DELETE FROM festivals"
    run_sql(sql)

def delete_by_id(id):
    sql = "DELETE FROM festivals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(festival):
    sql = "UPDATE festivals SET (name, country_id) = (%s, %s) WHERE id = %s"
    values = [festival.name, festival.country.id, festival.id]
    run_sql(sql, values)