from base import *

# URL TO PULL JSON DATA FROM. MUST BE DONE USING INSPECT ELEMENT
url = ""  

#EMAIL AND PASSWORD USED TO LOG IN
email = "email@gmail.com"
password = "password"

auth = base(url,email,password)

jsonRes = auth.ExcecuteLogin()

print(jsonRes.text)
