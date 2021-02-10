from db.run_sql import run_sql

from models.attendee import Attendee

import repositories.user_repository as user_repository
import repositories.festival_repository as festival_repository

def save(attendee):
    sql = "INSERT INTO attendees ( user_id, festival_id) VALUES (%s, %s) RETURNING *"
    values = [attendee.user.id, attendee.festival.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    attendee.id = id
    return attendee

def select_all():
    attendees = []

    sql = "SELECT * FROM attendees"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select_by_id(row['user_id'])
        festival = festival_repository.select_by_id(row['festival_id'])
        attendee = Attendee(user, festival, row['id'])
        attendees.append(attendee)
    return attendees

def delete_all():
    sql = "DELETE * FROM attendees"
    run_sql(sql)

def delete_by_id(id):
    sql = "DELETE FORM attendees WHERE id = %s"
    values = [id]
    run_sql(sql, values)