import requests

class base:
    def __init__ (self,targetUrl: str, email:str,password:str):
        '''
        Constructor for base class
        '''
        self.targetUrl = targetUrl
        self.email = email
        self.password = password
        self.session =requests.Session()

    def Login(self):
        """
        - Takes -> Email | Password from constructor
        - Writes token to "token.txt" file
        - Returns status code and if there is an error with the code it will return 500
        """
        try:
            url = "https://discord.com/api/v9/auth/login"

            payload = {
                "captcha_key":None,
                "login_source":None,
                'login':self.email,
                'password': self.password,
                'undelete': False
            }

            response = self.session.post(url,json=payload)
            status_code = response.status_code
            if status_code != 401: 
                with open("token.txt", "w") as file:
                    file.write(response.json()['token'])
            return status_code
        except:
            print("Error has occured")
            return 500
    
    def Authorization(self):
        '''
        - Takes -> Target Url 
        - Reads "token.txt" file
        - Tries to connect to discord using token
        - Returns response
        '''
        try:
            with open("token.txt", "r") as file:
                token = file.read()
                if token.strip() == "":
                    self.Login()
                    with open("token.txt", "r") as file:
                        token = file.read()
        except FileNotFoundError:
            self.Login()
            with open("token.txt", "r") as file:
                token = file.read()

        try:
            data = {
                'authorization': token
            }

            response = self.session.get(self.targetUrl, headers=data)
            return response
        except:
            return 401


    def ExcecuteLogin(self):
        '''
        - Errorchecking method
        - If authorization fails -> login again and return the authorization response
        '''
        authResponse = self.Authorization()

        if (authResponse == 401):
            print("Invalid login credentials/url")
            return
        if (authResponse.status_code != 401):
            return authResponse
        else:
            self.Login()
            return self.Authorization()