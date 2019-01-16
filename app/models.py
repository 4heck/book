from app import db
import re

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee = db.Column(db.Integer)
    company = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    locality = db.Column(db.Integer)

    def to_dict(self):
        dict = {
        'employee': self.employee,
        'company': self.company,
        'salary': self.salary,
        'locality': self.locality
        }
        return dict

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))

    def to_dict(self):
        dict = {
        'name': self.name
        }
        return dict

class Town(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(300))
    area = db.Column(db.String(300))
    locality = db.Column(db.String(300))

    def to_dict(self):
        dict = {
        'region': self.region,
        'area': self.area,
        'locality': self.locality
        }
        return dict

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))

    def to_dict(self):
        dict = {
        'name': self.name
        }
        return dict