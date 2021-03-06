from db.run_sql import run_sql

from models.user import User
from models.attendee import Attendee
from models.festival import Festival

def save(user):
    sql = "INSERT INTO users (first_name, last_name, age) VALUES (%s, %s, %s) RETURNING *"
    values = [user.first_name, user.last_name, user.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['first_name'], row['last_name'], row['age'], row['id'])
        users.append(user)
    return users

def select_by_id(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['first_name'], result['last_name'], result['age'], result['id'])
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete_by_id(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(user):
    sql = "UPDATE users SET (first_name, last_name, age) = (%s, %s, %s) WHERE id = %s"
    values = [user.first_name, user.last_name, user.age, user.id]
    run_sql(sql, values)


def festivals(user):
    festivals = []

    sql = "SELECT festivals.* FROM festivals INNER JOIN attendees ON attendees.festival_id = festivals.id WHERE user_id = %s;"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        festival = Festival(row['name'], row['id'])
        festivals.append(festival)

    return festivals