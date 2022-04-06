from datetime import date, datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):

    current_date_object = datetime.strptime(current_date, "%B %d, %Y")
    expiration_date_object = datetime.strptime(expiration_date, "%B %d, %Y")
    print(current_date_object)
    print(expiration_date_object)
    if expiration_date_object >= current_date_object  and entered_code == correct_code:
        print('True')
    else:
        print('False')


# check_coupon('123','123','September 5, 2014','October 1, 2014')
# check_coupon('123a','123','September 5, 2014','October 1, 2014')
check_coupon("123", "123", "July 9, 2015", "July 2, 2015")
# check_coupon("123", "123", "July 9, 2015", "July 9, 2015")
