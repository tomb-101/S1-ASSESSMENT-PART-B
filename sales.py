import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''
    sold_today=random.randint(1, 200)
    if current_day%7!=0 and (available_items>0 or available_items==2000):
        available_items-=sold_today
        contain=(current_day, sold_today, 0, available_items)
        inventory_records.append(contain)
    return available_items