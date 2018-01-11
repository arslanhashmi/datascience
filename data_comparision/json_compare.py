import json



data1 = {
    'number' : 2,
    'string' : 'i am arslan',
    'float': 23.3,
    'list': [1,3,4],
    'dict': {
        'a':2,
        #'n':[]
    },
    'outlets': [
        {
            'id': 1465,
            "lat": 25.24181,
            "human_location": "Ground Level",
            "merchant": {
                    "id": 928,
                    "name": "Nomad",
                    "categories": [
                        "Restaurants and Bars"
                    ],
                    "categories_analytics": "FD",
                    "cuisines": [
                        "International"
                    ],
            }
        }
            ]
}

data2 = {
    'number' : 2,
    'string' : 'i am arslan',
    'float': 23.3,
    'list': [1,3,4],
    'dict': {
            'a':2,
            #'n': 3
        },
    'outlets': [
        {
            'id': 1465,
            "lat": 25.24181,
            "human_location": "Ground Level",
            "merchant": {
                    "id": 928,
                    "name": "Nomad",
                    "categories": [
                        "Restaurants and Bars",

                    ],
                    "categories_analytics": "FD",
                    "cuisines": [
                        "International"
                    ],
            },

        }
    ]

}
data3 = {
        "id": 30035,
        "sfId": "O22759180",
        "name": "Hazelwood",
        "email": "",
        "telephone": "+27 12 346 2265",
        "lat": -25.778355,
        "lng": 28.257021,
        "human_location": "The Club, Corner of Pinaster & Dely Avenue",
        "neighborhood": "Hazelwood",
        "mall": "",
        "hotel": "",
        "tripadvisor_id": "9999",
        "distance": 6252013,
        "description": "",
        "merchant_name": "Knead",
        "merchant": {
            "id": 2230,
            "name": "Knead",
            "name_for_outlet": "Knead",
            "description": "",
            "category": "Restaurants and Bars",
            "cuisine": "",
            "digital_section": "Modern & Contemporary",
            "ad_travel_country": "",
            "ad_active_status": 0,
            "logo_url": "https://s3.amazonaws.com/offer-engine/knead-x036629/merchant_primary_logo_%28retina%29_-_merchant.png",
            "logo_small_url": "https://s3.amazonaws.com/offer-engine/knead-x036629/merchant_primary_logo_%28non-retina%29_-_merchant.png",
            "photo_url": "https://s3.amazonaws.com/offer-engine/knead-x036629/merchant_profile_%22hero%22_image_%28retina%29.png",
            "photo_small_url": "https://s3.amazonaws.com/offer-engine/knead-x036629/merchant_profile_%22hero%22_image_%28non-retina%29.png"
        },
        "fuzzy_relevance": 0,
        "top_offer_redeemability": 0,
        "top_offer_type": 0,
        "is_purchased": False,
        "is_shared": False,
        "is_more_sa": False,
        "is_cheers": False,
        "is_delivery": False,
        "top_up_offer": False,
        "offer_types_included": []
    }


data4 = {
                "top_offer_type": 0,
                "offer_types_included": [],
                "hotel": "",
                "is_new": False,
                "is_monthly": False,
                "top_up_offer": False,
                "telephone": "+27 12 346 2265",
                "name": "Hazelwood",
                "mall": "",
                "is_more_sa": False,
                "human_location": "The Club, Corner of Pinaster & Dely Avenue",
                "sfId": "O22759180",
                "distance": 6252013,
                "is_purchased": False,
                "description": "",
                "top_offer_redeemability": 0,
                "fuzzy_relevance": 0,
                "id": 30035,
                "is_redeemable": False,
                "lat": -25.778355,
                "neighborhood": "Hazelwood",
                "is_cheers": 0,
                "email": "",
                "tripadvisor_id": 9999,
                "lng": 28.257021,
                "merchant": {
                    "category": "Restaurants and Bars",
                    "id": 2230,
                    "photo_url": "https://s3.amazonaws.com/offer-engine/knead-x036629/merchant_profile_%22hero%22_image_%28retina%29.png",
                    "logo_small_url": "https://s3.amazonaws.com/offer-engine/knead-x036629/merchant_primary_logo_%28non-retina%29_-_merchant.png",
                    "name_for_outlet": "Knead",
                    "name": "Knead",
                    "ad_active_status": 0,
                    "ad_travel_country": "",
                    "digital_section": "Modern & Contemporary",
                    "cuisine": "",
                    "description": "",
                    "photo_small_url": "https://s3.amazonaws.com/offer-engine/knead-x036629/merchant_profile_%22hero%22_image_%28non-retina%29.png",
                    "logo_url": "https://s3.amazonaws.com/offer-engine/knead-x036629/merchant_primary_logo_%28retina%29_-_merchant.png"
                },
                "is_delivery": 0,
                "merchant_name": "Knead",
                "is_shared": False
            }
json_data1 = json.dumps(data3)
json_data2 = json.dumps(data4)

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

def check_and_compare_lists(list1, list2,key):
    if len(list1) == 0 and len(list2) == 0:
        return
    if key == 'outlets':
        print('Outlets in both are',len(list1),len(list2))
        id1 = []
        id2 = []
        for l1,l2 in zip(list1,list2):
            id1.append(l1['id'])
            id2.append(l2['id'])
        id1.sort()
        id2.sort()
        print(id1)
        print(id2)
        #return False

    monitoring_list1 = all ( isinstance ( x, (int, bool, str, float) ) for x in list1 )
    monitoring_list2 = all ( isinstance ( x, (int, bool, str, float) ) for x in list2 )
    monitoring_dict_list1 = all ( isinstance ( x, (dict) ) for x in list1 )
    monitoring_dict_list2 = all ( isinstance ( x, (dict) ) for x in list2 )
    if monitoring_dict_list1 and monitoring_dict_list2:
        if key != 'offers' and key !='merchant_attributes':
            try :
                keys = 'id' if 'id' in list1[0] else 'offer_id'
                if key == 'attributes':
                    keys = 'key'
                print('----' , key, 'is going to be sorted on the basic of', keys,'----')
                from operator import itemgetter
                list1 = sorted ( list1, key=itemgetter (keys) )
                list2 = sorted (list2, key=itemgetter (keys))
            except:
                print("Can't find id or offer_id in the list of dictionaries to be sorted.")
                print('The key was',key)
                return False

    if not monitoring_list1 and not monitoring_list2 and len ( list1 ) == len ( list2 ):
        for val1, val2 in zip ( list1, list2 ):
            if type ( val1 ) == type ( val2 ):
                if isinstance ( val1, (list, set) ):
                    check_and_compare_lists(val1, val2)
                elif isinstance ( val1, (dict, json) ):
                    correct_result = compare_data ( val1, val2 )
                    if not correct_result:
                        correct_status = False
            else:
                print ( 'Type of', val1, 'and', val2, 'do not match.' )
    elif len ( list1 ) != len ( list2 ):
        print('Length of ',key,"do not match so can't be checked")
        #compare_data(list1,list2) # this needs to be monitored
    else:
        comparision = compare_lists ( list1, list2, 'element not present in comparision of list for attribute:' + key )



def compare_data (dict1, dict2):
    correct_status = True
    difference = compare_lists(dict1.keys(), dict2.keys(), 'difference in keys of document')

    for key,value in dict1.items():
        try:
            if type(value) != type(dict2[key]):
                print('Value types do not match for attribute:',key,'clash is between',type(value),'and',type(dict2[key]))
                #return False
        except Exception as e:
            print(e)
        if isinstance(value, (int,str,float,bool)):
            try:
                if value != dict2[key]:
                    correct_status = False
                    print('Value do not match for attribute', key, 'clash is between', value, 'and', dict2[key])
            except Exception as e:
                print(e)
        elif isinstance(value, (list,set)):
            try:
                check_and_compare_lists(value, dict2[key],key)
            except Exception as e:
                print(e)
        elif isinstance(value, (dict,json)):
            correct_result = compare_data(value, dict2[key])
            if not correct_result:
                pass
                #correct_status = False
    return correct_status

if __name__ == '__main__':
    print(compare_data(back_dict1, back_dict2))
    #print(back_dict1.keys())
