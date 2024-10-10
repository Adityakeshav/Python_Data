def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item['price']*item['qantity']
    return total_cost
cart=[
    {'name':'Iphone','price':80000,'qantity':4},
    {'name':'Samsung','price':100000,'qantity':5},
    {'name':'OnePlus','price':50000,'qantity':10}
]


print(calculate_total_cost(cart))