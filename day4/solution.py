import hashlib
key = "iwrupvqb"

for i in range(int(1e10)):
    h = hashlib.md5("{}{}".format(key,i).encode('utf-8')).hexdigest()
    if h[:6] == '000000':
        print(i)
        break
