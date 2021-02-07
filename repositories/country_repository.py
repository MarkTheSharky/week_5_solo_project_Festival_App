from db.run_sql import run_sql

from models.country import Country

def save(country):
    sql = "INSERT INTO countries (name, country_code) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.country_code]
    results = run_sql(sql, values)
    id = results[0]["id"]
    country.id = id
    return country

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['country_code'], row['id'])
        countries.append(country)
    return countries

def select_buy_id(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['country_code'], result['id'])
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete_by_id(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE countries SET (name, country_code) = (%s, %s) WHERE id= %s"
    values = [country.name, country.country_code, country.id]
    run_sql(sql, values)