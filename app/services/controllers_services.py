
from datetime import datetime


def data_is_checked(**data) -> bool:

    name = data['name']
    email = data['email']
    phone = data['phone']

    if (name and email and verify_phone(phone)):
        return True
    if not verify_phone(phone):
        raise ValueError

def verify_phone(phone:str)-> bool:
    if (len(phone) == 14 and
        phone[0] =='(' and
        phone[3] == ')' and
        phone[1:3].isnumeric() and
        phone[4:9].isnumeric() and
        phone[10:].isnumeric() and
        phone[9] == '-'):
        return True
    return False

def verify_email(**data) -> bool:
    if len(data.keys())==1 and type(data['email']) is str:
        return True
    return False

def att_register(register) -> None:
    now = datetime.now()
    setattr(register,'last_visit',now)
    setattr(register,'visits',register.visits + 1)
