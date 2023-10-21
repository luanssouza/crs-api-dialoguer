from utils.database import session_factory
from models.answer import Answer

def insert_answer_dict(obj_dict):
    session = session_factory()

    obj = Answer(**obj_dict)
    session.add(obj)

    session.flush()
    obj_id = obj.id
    
    session.commit()
    session.close()

    return obj_id