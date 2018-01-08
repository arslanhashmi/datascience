
import json



data1 = {
    'number' : 2,
    'string' : 'i am arslan',
    'float': 23.3,
    'list': [1,3,4],
    'dict': {
        'a':2,
    }
}

data2 = {
    'number' : 2,
    'string' : 'i am arslan',
    'float': 23.3,
    'list': [1,3,4,5],
    'dict': {
            'a':2
        }

}

json_data1 = json.dumps(data1)
json_data2 = json.dumps(data2)

back_dict1 = json.loads(json_data1)
back_dict2 = json.loads(json_data2)

def compare_lists(list_1, list_2, mete_data):
    difference1 = set(list_1) - set(list_2)
    difference2 = set(list_2) - set(list_1)
    if difference1:
        print(difference1,mete_data)
    if difference2:
        print(difference2,mete_data)
    return True if difference1 or difference2 else False

def compare_data (dict1, dict2):
    correct_status = True
    difference = compare_lists(dict1.keys(), dict2.keys(), 'difference in keys of document')
    if difference:
        return False
    for key,value in dict1.items():
        if type(value) != type(dict2[key]):
            print('Value types donot match for attribute:',key,'clash is between',type(value),'and',type(dict2[key]))
            return False
        if isinstance(value, (int,str,float)):
            if value != dict2[key]:
                correct_status = False
                print('Value donot match for attribute', key, 'clash is between', value, 'and', dict2[key])
        elif isinstance(value, (list,set)):
            compare_lists(value, dict2[key], 'difference in comparision of list for attribute:'+key)
        elif isinstance(value, (dict,json)):
            correct_result = compare_data(value, dict2[key])
            if not correct_result:
                correct_status = False
    return correct_status

print(compare_data(back_dict1, back_dict2))