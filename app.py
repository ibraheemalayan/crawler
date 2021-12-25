from requests import get

from models import session, Order
from sqlalchemy.exc import IntegrityError


def update_from_site():
    
    res  = get("https://haatdashboardbackend.azurewebsites.net/api/Campaign/OrdersMilestone").json()
    
    for order in res['orders']:
        
        new_order = Order(
            id=int(order['id']),
            region_ar=str(order['area_ar']),
            region_en=str(order['area_en']),
            price=int(order['price'])
        )
        
        try:
            session.add(new_order)
            session.commit()
            print(f"    ✔ Added Order {new_order.id}")
        except IntegrityError as e:
            print("❌")
            session.rollback()
        print(order)
    # print(res)
    


import time
starttime = time.time()
while True:
    print("update > ")
    
    update_from_site()
    
    
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))