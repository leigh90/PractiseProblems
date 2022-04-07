# def evaporator(content, evap_per_day, threshold):
#     days = 0
# 	new_func(content, evap_per_day, threshold, days)

def evaporator(content, evap_per_day, threshold):
    days = 0
    threshold_in_ml = threshold/100 * content
    print(threshold_in_ml)
    while content > (threshold_in_ml):          
        loss_per_day = evap_per_day / 100 * content
    #     # import pdb; pdb.set_trace()
        content = content - loss_per_day
        print(content)
        days += 1
    print(days)


evaporator(10, 10, 10)