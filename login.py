import requests
import unittest
import read_login_data
from parameterized import parameterized

import api
class Test_login(unittest.TestCase):
    def setUp(self):

        self.req=requests
        self.Login=api.Login()

    @parameterized.expand(read_login_data.read())
    def test_login(self,username,password,verify_code):
        url="http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.7879911219754482"

        respose=self.Login.login(self.req,url,username,password,verify_code)

        cook=respose.cookies.get("PHPSESSID")
        print(username, password, verify_code)

        self.cookie={"PHPSESSID":cook}
        print(respose.json().get("msg"))


        self.assertEqual("登陆成功",respose.json().get("msg"))

        # try:
        #
        #     self.assertEqual("登陆成功",respose.json().get("msg"))
        # except Exception as e:
        #     print(username, password, verify_code)




    @parameterized.expand(read_login_data.read())
    def test_see(self,username,password,verify_code):
        url = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.7879911219754482"
        respose=self.Login.login(self.req,url,username,password,verify_code)
        cook = respose.cookies.get("PHPSESSID")
        print(username,password,verify_code)
        cookie = {"PHPSESSID": cook}


        url="http://www.testingedu.com.cn:8000/index.php?m=Home&c=Cart&a=header_cart_list"
        respose=self.Login.see_login(self.req,url,cookie)
        self.assertEqual(200, respose.status_code)

        print(respose.text)
if __name__ == '__main__':
    unittest.main()