import pdb

def get_name(person):
    return person["name"]


def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]


def likes_to_eat(person, food):
    snack_list = person["favourites"]["snacks"]
    for item in snack_list:
        if item == food:
            return True
        
    return False 

def add_friend(person_dict, friend_to_be_added):
    place_to_add = person_dict["friends"]
    place_to_add.append(friend_to_be_added) 


def remove_friend(person_dict, friend_to_be_removed):
    place_to_remove = person_dict["friends"]
    place_to_remove.remove(friend_to_be_removed)


def total_money(person_list):
    add_money = 0
    for person in person_list:
        add_money += person["monies"]
    return add_money

def l_money(person1, person2, value_of_loan):    
    person1["monies"] -= value_of_loan
    person2["monies"] += value_of_loan


def all_favourite_foods(people_list):
    #pdb.set_trace()
    everyone_fav_foods = []
    
    for person in people_list:
        for food in person["favourites"]["snacks"]:           
            everyone_fav_foods.append(food)

    return everyone_fav_foods







