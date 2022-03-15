import re

def remove_url_anchor(url):
    x = re.search("#", url)
    if x == None:
        return url
    else:
        return url[0:x.start()]



remove_url_anchor("www.codewars.com?page=1")   

# other ways
def remove_url_anchor(url):
    print(url.partition('#')[0])
    # partition() method returns a tuple with 3 parts, the part before the match, the match and the part after
    # this returns the part before that part
