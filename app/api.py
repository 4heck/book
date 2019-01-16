from app import app
from models import Ad
from models import Employee
from models import Town
from models import Company
from flask import jsonify
from flask import request
from app import db
import json

#api's for ad
@app.route('/api/ad', methods=['GET'])
def api_ad_get():
    ads = Ad.query.all()
    ads_json = [{"id": ad.id, "employee": ad.employee, "company": ad.company, "salary": ad.salary, "locality": ad.locality}
                  for ad in ads]
    return jsonify(ads_json)

@app.route('/api/ad/<id>', methods=['GET'])
def api_ad_get_id(id):
    ads = Ad.query.filter_by(id=id)
    if not ads:
        abort(404)
    ad = ads[0]
    ad_json = {"id": ad.id, "employee": ad.employee, "company": ad.company, "salary": ad.salary, "locality": ad.locality}
    return jsonify(ad_json)

@app.route('/api/ad', methods=['POST'])
def api_ad_insert():
    new_ad = request.get_json()
    ad = Ad(id=new_ad['id'], employee=new_ad['employee'], company=new_ad['company'], salary=new_ad['salary'], locality=new_ad['locality'])
    db.session.add(ad)
    db.session.commit()
    ad_json = {"id": ad.id, "employee": ad.employee, "company": ad.company, "salary": ad.salary, "locality": ad.locality}
    return jsonify(ad_json)

@app.route('/api/ad/<id>', methods=['DELETE'])
def api_ad_delete(id):
    ads = Ad.query.filter_by(id=id)
    if not ads:
        abort(404)
    ad = ads[0]
    db.session.delete(ad)
    db.session.commit()
    return jsonify()

@app.route('/api/ad/<id>', methods=['PUT'])
def api_ad_update(id):
    updated_ad = request.get_json()
    ads_to_update = Ad.query.filter_by(id=id)
    data = json.loads(request.get_data())
    ad_to_update = ads_to_update[0]
    ad_to_update = db.session.query(Ad).filter_by(id = id).first()
    ad_to_update.employee = data['employee']
    ad_to_update.company = data['company']
    ad_to_update.salary = data['salary']
    ad_to_update.locality = data['locality']
    db.session.commit()
    return jsonify(ad_to_update.to_dict())

#api's for employee
@app.route('/api/employee', methods=['GET'])
def api_employee_get():
    employees = Employee.query.all()
    employees_json = [{"id": employee.id, "name": employee.name}
                  for employee in employees]
    return jsonify(employees_json)

@app.route('/api/employee/<id>', methods=['GET'])
def api_employee_get_id(id):
    employees = Employee.query.filter_by(id=id)
    if not employees:
        abort(404)
    employee = employees[0]
    employee_json = {"id": employee.id, "name": employee.name}
    return jsonify(employee_json)

@app.route('/api/employee', methods=['POST'])
def api_employee_insert():
    new_employee = request.get_json()
    employee = Employee(id=new_employee['id'], name=new_employee['name'])
    db.session.add(employee)
    db.session.commit()
    employee_json = {"id": employee.id, "name": employee.name}
    return jsonify(employee_json)

@app.route('/api/employee/<id>', methods=['DELETE'])
def api_employee_delete(id):
    employees = Employee.query.filter_by(id=id)
    if not employees:
        abort(404)
    employee = employees[0]
    db.session.delete(employee)
    db.session.commit()
    return jsonify()

@app.route('/api/employee/<id>', methods=['PUT'])
def api_employee_update(id):
    updated_employee = request.get_json()
    employees_to_update = Employee.query.filter_by(id=id)
    data = json.loads(request.get_data())
    employee_to_update = employees_to_update[0]
    employee_to_update = db.session.query(Employee).filter_by(id = id).first()
    employee_to_update.name = data['name']
    db.session.commit()
    return jsonify(employee_to_update.to_dict())

#api's for company
@app.route('/api/company', methods=['GET'])
def api_company_get():
    companys = Company.query.all()
    companys_json = [{"id": company.id, "name": company.name}
                  for company in companys]
    return jsonify(companys_json)

@app.route('/api/company/<id>', methods=['GET'])
def api_company_get_id(id):
    companys = Company.query.filter_by(id=id)
    if not companys:
        abort(404)
    company = companys[0]
    company_json = {"id": company.id, "name": company.name}
    return jsonify(company_json)

@app.route('/api/company', methods=['POST'])
def api_company_insert():
    new_company = request.get_json()
    company = Company(id=new_company['id'], name=new_company['name'])
    db.session.add(company)
    db.session.commit()
    company_json = {"id": company.id, "name": company.name}
    return jsonify(company_json)

@app.route('/api/company/<id>', methods=['DELETE'])
def api_company_delete(id):
    companys = Company.query.filter_by(id=id)
    if not companys:
        abort(404)
    company = companys[0]
    db.session.delete(company)
    db.session.commit()
    return jsonify()

@app.route('/api/company/<id>', methods=['PUT'])
def api_company_update(id):
    updated_company = request.get_json()
    companys_to_update = Company.query.filter_by(id=id)
    data = json.loads(request.get_data())
    company_to_update = companys_to_update[0]
    company_to_update = db.session.query(Company).filter_by(id = id).first()
    company_to_update.name = data['name']
    db.session.commit()
    return jsonify(company_to_update.to_dict())

#api's for town
@app.route('/api/town', methods=['GET'])
def api_town_get():
    towns = Town.query.all()
    towns_json = [{"id": town.id, "region": town.region, "area": town.area, "locality": town.locality}
                  for town in towns]
    return jsonify(towns_json)

@app.route('/api/town/<id>', methods=['GET'])
def api_town_get_id(id):
    towns = Town.query.filter_by(id=id)
    if not towns:
        abort(404)
    town = towns[0]
    town_json = {"id": town.id, "region": town.region, "area": town.area, "locality": town.locality}
    return jsonify(town_json)

@app.route('/api/town', methods=['POST'])
def api_town_insert():
    new_town = request.get_json()
    town = Town(id=new_town['id'], region=new_town['region'], area=new_town['area'], locality=new_town['locality'])
    db.session.add(town)
    db.session.commit()
    town_json = {"id": town.id, "region": town.region, "area": town.area, "locality": town.locality}
    return jsonify(town_json)

@app.route('/api/town/<id>', methods=['DELETE'])
def api_town_delete(id):
    towns = Town.query.filter_by(id=id)
    if not towns:
        abort(404)
    town = towns[0]
    db.session.delete(town)
    db.session.commit()
    return jsonify()

@app.route('/api/town/<id>', methods=['PUT'])
def api_town_update(id):
    updated_town = request.get_json()
    towns_to_update = Town.query.filter_by(id=id)
    data = json.loads(request.get_data())
    town_to_update = towns_to_update[0]
    town_to_update = db.session.query(Town).filter_by(id = id).first()
    town_to_update.region = data['region']
    town_to_update.area = data['area']
    town_to_update.locality = data['locality']
    db.session.commit()
    return jsonify(town_to_update.to_dict())