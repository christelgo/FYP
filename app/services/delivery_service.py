# CBD area surcharges
CBD_POSTAL_DISTRICT=[ (1,5), (7,8),(17,19),(22,22)]

CBD_SURCHARGE = 4.00

def in_cbd_area(postal_code):
    try:
        district = int(str(postal_code)[:2])
    except:
        return False
    
    for start, end in CBD_POSTAL_DISTRICT:
        if start <= district <=end:
            return True
        
    return False

#mock up version of delivery rates that mimics lalamoves actual policy
def get_lalamove_price(order):
    zone = order["zone"]
    postal_code = order.get("postal_code")
    
    base_rate = {
        "West": 5.50,
        "Central": 6.70,
        "East": 7.00
    }

    base_fee = base_rate.get(zone, 0)

    cbd_surcharge = CBD_SURCHARGE if in_cbd_area(postal_code) else 0
    
    total_fee= base_fee + cbd_surcharge


    return {
        "provider": "LALAMOVE",
        "base_fee": base_fee,
        "cbd_surcharge": cbd_surcharge,
        "is_cbd": cbd_surcharge > 0,
        "fee": round(total_fee,2)
    }



