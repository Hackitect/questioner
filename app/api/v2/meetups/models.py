import psycopg2
import datetime
from app.api.v2.utils import database
from app.api.v2.utils.validators import Validators
from flask import json, jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,
                                get_jwt_identity, jwt_refresh_token_required)

db = database.Database()
cursor = db.cursor()
now = datetime.datetime.now()

class Meetup():
    def __init__(self, topic, location, tags, happening_on):
        self.topic = topic
        self.location = location
        self.tags = tags
        self.happening_on = happening_on
        self.created_on = now

    def meetup_exists(self, topic):
        sql = """SELECT * from meetups WHERE topic=%s;"""
        cursor.execute(sql, (topic,))
        topic = cursor.fetchone()
        if topic:
            return True
    
    def create_meetup(self):
        if self.meetup_exists(self.topic):
            return {"msg": "meetup already exists with that topic"}
        sql = """INSERT INTO meetups (topic, location, tags, happening_on, created_on) \
                                        values(%s,%s,%s,%s,%s) returning meetup_id;"""
        cursor.execute(sql,
            (self.topic,
            self.location,
            self.tags,
            self.happening_on,
            self.created_on)
            )
        meetup = cursor.fetchone()
        db.conn.commit()
        return meetup

    @staticmethod
    def delete_meetup(meetup_id):
        sql = """DELETE * from meetups WHERE meetup_id=%s;"""
        cursor.execute(sql, (meetup_id))
        db.conn.commit()