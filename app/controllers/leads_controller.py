from datetime import datetime
from flask import current_app,jsonify,request
from sqlalchemy.exc import IntegrityError,NoResultFound
from http import HTTPStatus

from app.models.leads_model import Leads
from app.services.controllers_services import data_is_checked,verify_email,att_register


def get_all_leads():

    leads_list = Leads.query.all()
    if leads_list:
        return jsonify(leads_list),HTTPStatus.OK
    return {"error": "Nem um dado encontrado!"},HTTPStatus.OK
  
def create_lead():

    data = request.get_json()
    try:
        if data_is_checked(**data):
            try:
                new_lead = Leads(**data)
                new_lead.creation_date = datetime.now()
                new_lead.last_visit = datetime.now()

                current_app.db.session.add(new_lead)
                current_app.db.session.commit()
    
                return jsonify(new_lead),HTTPStatus.CREATED
        
            except IntegrityError:
                return {"error": "esse email já está cadastrado"},HTTPStatus.CONFLICT
    except ValueError:
        return {"error": "O campo Phone deve ser no formato (xx)xxxxx-xxxx"},HTTPStatus.BAD_REQUEST
    except KeyError:
        return {"error": "Os campos 'name, email, phone' são obrigatórios"},HTTPStatus.BAD_REQUEST


def path_lead():
    data = request.get_json()
    try:
        if verify_email(**data):
            register = Leads.query.filter(Leads.email == data['email']).one()
            att_register(register)

            current_app.db.session.add(register)
            current_app.db.session.commit()
            
            return jsonify(register),HTTPStatus.OK
        return {"error": """Formato esperado {'email':string}"""},HTTPStatus.BAD_REQUEST
    except NoResultFound:
        return {"error": "o Email informado não foi encontrado"},HTTPStatus.NOT_FOUND
    except KeyError:
        return {"error": "O campo email é obrigatório"},HTTPStatus.BAD_REQUEST

def delete_lead():
    data = request.get_json()
    try:
        if verify_email(**data):
            register = Leads.query.filter(Leads.email == data['email']).one()
            current_app.db.session.delete(register)
            current_app.db.session.commit()
            
            return '',HTTPStatus.NO_CONTENT
        return {"error": """Formato esperado {'email':string}"""},HTTPStatus.BAD_REQUEST
    except NoResultFound:
        return {"error": "o Email informado não foi encontrado"},HTTPStatus.NOT_FOUND
    except KeyError:
        return {"error": "O campo email é obrigatório"},HTTPStatus.BAD_REQUEST
