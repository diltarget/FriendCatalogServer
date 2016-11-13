import json
import personality_insights
import random # test

# Make a problem

def define_columns():
    """
    Returns dictionary defining columns portion of json
    traits and preferences should be input
    :return:
    """
    columns = []
    # Get as input for traits
    traits = [{'name': 'Conscientiousness', 'low': 0, 'high': 1},
              {'name': 'Agreeableness', 'low': 0, 'high': 1},
              {'name': 'Emotional range', 'low': 0, 'high': 1},
              {'name': 'Extraversion', 'low': 0, 'high': 1},
              {'name': 'Openness', 'low': 0, 'high': 1}
              ]
    for trait in traits:
        trait_dic = {}
        trait_dic["key"] = trait['name'].lower().replace(" ", "_")
        trait_dic["type"] = "numeric"
        trait_dic["goal"] = "min" # What should this be? Minimize or maximize the objective function?
        trait_dic["range"] = {"low": trait['low'], 'high': trait['high']}
        trait_dic["format"] = "number:3"
        columns.append(trait_dic)
    categories = ['music', 'movies', 'color', 'sports']
    for category in categories:
        cat_dic = {}
        cat_dic["key"] = category
        cat_dic["type"] = "categorical"
        cat_dic["is_objective"] = True
        if category == 'music':
            kinds = ['rap', 'country', "rock", "metal", "classical", "jazz", "electronica", "pop"]
        elif category == 'movies':
            kinds = ['romance', 'horror', 'historical', 'scifi', 'war', 'drama', 'comedy', 'action', 'documentary']
        elif category == 'color':
            kinds = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'black', 'white']
        elif category == 'sports':
            kinds = ['baseball', 'basketball', 'football', 'soccer', 'tennis', 'golf', 'none']
        else:
            kinds = []
        cat_dic["range"] = kinds
        # get preferences - random from now, should be input
        skinds = kinds[:]
        random.shuffle(skinds)
        preferences = skinds[0:2]
        cat_dic["preference"] = list(preferences)
        columns.append(cat_dic)
    return {"columns": columns}
#    jdump = json.dumps({"columns": columns}, sort_keys=True, indent=4)
#    return jdump

def define_options():
    columns = define_columns()
    options = {'options': []}
    subject = {'subject': 'friendcatalog'}
    data = {**subject, **columns, **options}
    jdump = json.dumps(data, sort_keys=True, indent=4)
    return jdump

print(define_options())
