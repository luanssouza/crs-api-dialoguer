import json

def get_entity(body): #pega entidade como filmes, atores, etc.

    try:
        data = ''
        with open("intent_entity_extraction", "r") as file:
            data = json.loads(file.read())

        intent = get_intent(body)

        entity = data.get(intent)[0].get("entity")
        
        entity_value = body.get("entities").get(entity+":"+entity)[0].get("name")
    except:
        entity_value = ''    
    return entity_value


def get_entity_value(body): # pega o valor da entidade movie=[nome do filme]
    try:
        entity = get_entity(body)
        try:
            entity_value = body.get("entities").get(entity + ":" + entity)[0].get("body")
        except:
            entity_value = body.get("entities").get('wit$age_of_person:age_of_person')[0].get("body")
    except:
        
        entity_value = ''
    return entity_value


def get_intent(body): #intenção do usuário
    try:
        intent = body.get("intents")[0].get("name")
    except:
        intent ='property'
    return intent

def try_except_entity(message,entity,value):
    try:
        entity = "@" + entity
        message = message.replace(entity, value)
    except:
        return message
    return message