import unittest
from time import sleep
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
class YouJiuye(unittest.TestCase):
    def setUp(self):
        self.chrome=webdriver.Chrome()
        self.chrome.get("http://xue.ujiuye.com/foreuser/login/")
    def longin(self,username,password):
        username_dl=self.chrome.find_element_by_id("username_dl")
        password_dl=self.chrome.find_element_by_id("password_dl")
        button=self.chrome.find_elements_by_class_name("loginbutton1")

        username_dl.send_keys(username)
        password_dl.send_keys(password)
        button[0].click()
        text=self.chrome.find_element_by_id("J_usernameTip").text
        return text
    def test_username_longin(self):
        text=self.longin("17603987065","123448780998")
        self.assertEqual("账户不存在",text,'提示内容错误')
    def test_password_longin(self):
        text=self.longin('17603987065',"123")
        self.assertEqual("密码应该在6-20之间！",text,"密码提示内容错误")
    def tearDown(self):
        sleep(10)
        self.chrome.close()
if __name__=='__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(YouJiuye("test_username_longin"))
    suite.addTest(YouJiuye("test_password_longin"))
    with open("report.html", "wb") as f:
        runner =HTMLTestRunner(
            stream=f,
            title='教学测试',
            description="就是一个教学测试"
        )
        runner.run(suite)
