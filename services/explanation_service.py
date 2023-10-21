from utils.database import session_factory
from models.explanation import Explanation

def insert_explanation_dict(obj_dict):
    session = session_factory()

    obj = Explanation(**obj_dict)
    session.add(obj)
    
    session.commit()
    session.close()