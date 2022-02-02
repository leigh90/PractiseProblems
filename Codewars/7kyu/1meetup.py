lst1 = [
  { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
  { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
  { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
  { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
]

js_devs_from_europe = 0


def count_devs():
    js_devs_from_europe = 0
    for dev in lst1:
        if dev['continent'] == "Europe" and dev["language"] == "JavaScript":
            js_devs_from_europe+=1
    print(js_devs_from_europe)
    return js_devs_from_europe

count_devs()

        


