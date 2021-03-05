def nb_year(p0, percent, aug, p):
    years = 0
    percent = percent / 100
    while p0 < p:
        end_year = p0 + (p0 * percent) + aug 
        p0 = end_year
        years += 1
        print(p0)
    print(years)
    
    




nb_year(1000,2,50,13000)