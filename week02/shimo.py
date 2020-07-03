import requests
import time
class Login(object):
    def __init__(self):
        self.headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Referer':'https://shimo.im/login?from=home',
        'origin':'https://shimo.im',
        'path':'/lizard-api/auth/password/login',
        'accept':'*/*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9',
        'content-length':'39',
        'content-type':'application/x-www-form-urlencoded; charset=utf-8',
        'x-requested-with':'XmlHttpRequest',
        'x-source':'lizard-desktop'
    }
        self.header2 = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'authority':'shimo.im',
            'path':'/lizard-api/users/me',
            'scheme':'https',
            'accept':'application/vnd.shimo.v2+json',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'zh-CN,zh;q=0.9',
            'cache-control':'no-cache',
            'referer':'https://shimo.im/dashboard/used',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin',
            'x-requested-with':'XmlHttpRequest'
        }

        self.login_url = 'https://shimo.im/login?from=home'
        self.post_url = 'https://shimo.im/lizard-api/auth/password/login'
        self.logined_url = 'https://shimo.im/lizard-api/users/me'
        self.session = requests.Session()
    def login(self,phone,password):
        post_data = {
            'login':phone,
            'password':password
        }
        r = self.session.post(self.post_url,data=post_data,headers=self.headers)
        time.sleep(5)
        try:
            response = requests.get(self.logined_url,headers=self.header2,cookies=r.cookies)
            data = response.json()
            print ('login success!')
            print (data)
        except Exception as e:
            print (e)


if __name__ == "__main__":
    login = Login()
    login.login(phone='18008030654',password='guangguang123')