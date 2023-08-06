import hashlib



def hash(input)->str:
    if input is None:
        return

    md5 = hashlib.md5()
    md5.update(input)
    return md5.hexdigest()

if __name__ == "__main__":
    hash_icon = "https://www.lfaticon.com/free-icon/url_1078454"
    print(hash(hash_icon))
