def dessert_lover(list_items):

    new_list = []

    for item in list_items:
        match item:
            case "jelly" | "cookie" | "cake" | "candy":
                new_list.append(item)
                new_list.append(item)
            case "carrot" | "celery" | "pepper" | "broccoli":
                pass
            case _:
                new_list.append(item)
    
    return new_list

list_items = ["bread","candy","pepper","cherry","date"]

print(dessert_lover(list_items))
