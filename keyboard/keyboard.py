def greet_keyboard(telegram):
    keyboard = [
        [telegram.KeyboardButton("I am 15 years old or less")],
        [telegram.KeyboardButton('I am between 16 and 17 years old')],
        [telegram.KeyboardButton('I am 18 or over')]
    ]
    return keyboard

def auth_keyboard(telegram):
    keyboard = [
        [telegram.KeyboardButton("I'm authorized")],
        [telegram.KeyboardButton("I'm not authorized")]
    ]
    return keyboard    

def rec_keyboard(telegram):
    keyboard = [
        [telegram.KeyboardButton('I liked the recommendation')],
        [telegram.KeyboardButton("I've already watched")],
        [telegram.KeyboardButton("I didn't like the recommendation")],
        [telegram.KeyboardButton("Explain this recommendation")]
    ]
    return keyboard

def explain_keyboard(telegram): 
    keyboard = [
        [telegram.KeyboardButton('I liked the recommendation')],
        [telegram.KeyboardButton("I didn't like the recommendation")]   
    ]
    return keyboard

def properties_keyboard(telegram, paginate):
    properties = paginate.get_page()

    keyboard = []

    [keyboard.append([telegram.KeyboardButton(i)]) for i in properties]

    if paginate.has_next():
        keyboard.append([telegram.KeyboardButton('Something else')])

    return keyboard

def attributes_keyboard(telegram, attributes):
    keyboard = []
    if len(attributes) > 4:    
        for i in attributes[:5]:
            value = str(i.get("id")) + ") " + i.get("object") + ' (' + i.get("property") + ')' + "\n"
            keyboard.append([telegram.KeyboardButton(value)])
        keyboard.append([telegram.KeyboardButton('Recommend')])
        keyboard.append([telegram.KeyboardButton('Something else')])
    else:
        for i in attributes:
            value = str(i.get("id")) + ") " + i.get("object") + ' (' + i.get("property") + ')' + "\n"
            keyboard.append([telegram.KeyboardButton(value)])
        keyboard.append([telegram.KeyboardButton('Recommend')])

    return keyboard

def liked_keyboard(telegram):
    keyboard = [
        [telegram.KeyboardButton("hello")],
        [telegram.KeyboardButton('Bye')]
    ]
    return keyboard

def back_page_keyboard(telegram, paginate):
    
    vector = paginate.get_page()
    
    keyboard = []
    try:
        for i in vector:
            value = str(i.get("id")) + ") " + i.get("object") + ' (' + i.get("property") + ')' + "\n"
            keyboard.append([telegram.KeyboardButton(value)])
        
        keyboard.append([telegram.KeyboardButton('Recommend')])

        keyboard.append([telegram.KeyboardButton('Something else')]) 
        
        if paginate.has_prev():
            keyboard.append([telegram.KeyboardButton('Back Page')])

    except:
        [keyboard.append([telegram.KeyboardButton(i)]) for i in vector]
    
        keyboard.append([telegram.KeyboardButton('Something else')]) 
        
        if paginate.has_prev():
            keyboard.append([telegram.KeyboardButton('Back Page')])   

    return keyboard  

def something_else_keyboard(telegram, paginate):
    
    vector = paginate.get_page()

    keyboard = []

    try:
        for i in vector:
            value = str(i.get("id")) + ") " + i.get("object") + ' (' + i.get("property") + ')' + "\n"
            keyboard.append([telegram.KeyboardButton(value)])
        
        keyboard.append([telegram.KeyboardButton('Recommend')])
        
        if paginate.has_next():
            keyboard.append([telegram.KeyboardButton('Something else')]) 

        keyboard.append([telegram.KeyboardButton('Back Page')])

    except:
        [keyboard.append([telegram.KeyboardButton(i)]) for i in vector]
    
        if paginate.has_next():
            keyboard.append([telegram.KeyboardButton('Something else')])

        keyboard.append([telegram.KeyboardButton('Back Page')])     

    return keyboard