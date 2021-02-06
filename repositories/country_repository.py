from db.run_sql import run_sql

from models.country import Country

def save(country):
    sql = "INSERT INTO countries (name, country_code) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.country_code]
    results = run_sql(sql, values)
    id = results[0]["id"]
    country.id = id
    return country

