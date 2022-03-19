def getDiceImage(side):
    match side:
        case 1:
            return one()
        case 2:
            return two()
        case 3:
            return three()
        case 4:
            return four()
        case 5:
            return five()
        case 6:
            return six()
        case _:
            return ""

def one():
    result  = " -----\n"
    result += "|     |\n"
    result += "|  o  |\n"
    result += "|     |\n"
    result += " ----- \n"
    return result

def two():
    result  = " ----- \n"
    result += "|o    |\n"
    result += "|     |\n"
    result += "|    o|\n"
    result += " ----- \n"
    return result

def three():
    result  = " ----- \n"
    result += "|o    |\n"
    result += "|  o  |\n"
    result += "|    o|\n"
    result += " ----- \n"
    return result

def four():
    result  = " ----- \n"
    result += "|o   o|\n"
    result += "|     |\n"
    result += "|o   o|\n"
    result += " ----- \n"
    return result

def five():
    result  = " ----- \n"
    result += "|o   o|\n"
    result += "|  o  |\n"
    result += "|o   o|\n"
    result += " ----- \n"
    return result

def six():
    result  = " ----- \n"
    result += "|o   o|\n"
    result += "|o   o|\n"
    result += "|o   o|\n"
    result += " ----- \n"
    return result