from models.category import Category

def get_all_categories(return_objects=False):
    categories = Category.read()

    if not return_objects:
        list_of_categories = [
            category.toJSON() for category in categories
        ]
        return list_of_categories

    return categories

def get_category_with_id(id, return_object=False):
    """
    Set return_object to True if you want to return a 
    model instance instead of JSON
    """
    category = Category.read(id)
    return category if return_object else category.toJSON()

def save_category(name, id=None):
    if id != None:
        # get category with id
        category = get_category_with_id(id, return_object=True)
        category.name = name

    else:
        category = Category(name=name)
    
    category.save()

    return category.toJSON()

def delete_subject(id):
    category = get_category_with_id(id, return_object=True)
    category.delete()

    return category.toJSON()
