
class Login():
    def login(self,requests,url1,username,password,verify_code):
        respose=requests.post(url=url1,data={"username":username,"password":password,"verify_code":verify_code})


        return respose

    def see_login(self,requests,url,cookie):




        req=requests.get(url=url,cookies=cookie)


        return req




