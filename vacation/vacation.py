def hotel_cost(nights):
    return 140* nights
def plane_ride_cost(city):
    if city == "Delhi":
        return 183
    elif city == "Mumbai":
        return 220
    elif city == "London":
        return 222
    elif city == "city of angels":
        return 475
def rental_car_cost(days):
    cost = days*40
    if days>=7 :
         cost -=50
    elif days>= 3:
            cost-=20
    else:
            cost = cost
    return cost 
def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+ hotel_cost(days)+plane_ride_cost(city)+spending_money
print trip_cost("city of angels",5,600)      