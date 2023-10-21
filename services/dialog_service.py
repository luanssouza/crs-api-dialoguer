from utils.database import session_factory
from models.dialog import Dialog

def get_last_dialog():
    session = session_factory()

    obj = session.query(Dialog).order_by(Dialog.id.desc()).first()

    session.close()

    return obj

def insert_dialog_dict(obj_dict):
    session = session_factory()

    obj = Dialog.fromdata(**obj_dict)
    session.add(obj)

    session.flush()
    obj_id = obj.id
    
    session.commit()
    session.close()

    return obj_id

def update_property_dialog_dict(id, prop):
    session = session_factory()

    session.query(Dialog).filter(Dialog.id == id).update({"property": prop})
    
    session.commit()
    session.close()

    return id

def update_object_dialog_dict(id, obj):
    session = session_factory()

    session.query(Dialog).filter(Dialog.id == id).update({"object": obj})
    
    session.commit()
    session.close()

    return id