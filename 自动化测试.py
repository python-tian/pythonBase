# from selenium import webdriver
# #实例化一个浏览器驱动
# chrome=webdriver.Chrome()
# #访问页面
# chrome.get("https://www.baidu.com/")
# #捕获元素
# inputs=chrome.find_element_by_id("kw")
# #对元素进行操作
# inputs.send_keys("老边饺子")
# button=chrome.find_element_by_id("su")
# button.click()
# #关闭浏览器
# # chrome.close()
# import unittest
# from time import sleep
# from selenium import webdriver
# class YouJiuyeTest(unittest.TestCase):
#     def setUp(self):
#         self.chrome=webdriver.Chrome()
#         self.chrome.get("http://xue.ujiuye.com/foreuser/login/")
#     def test_login_password(self):
#         username_d1=self.chrome.find_element_by_id("username_dl")
#         password_d1=self.chrome.find_element_by_id("password_dl")
#         button=self.chrome.find_elements_by_class_name("loginbutton1")
#
#
#         username_d1.send_keys("17603987065")
#         password_d1.send_keys("123")
#         button[0].click()
#
#         text=self.chrome.find_element_by_id("J_usernameTip").text
#         self.assertEqual("密码应该为6-20之间！",text,"密码太短提示内容有误")
#     def test_login_username(self):
#         username_d1=self.chrome.find_element_by_id("username_dl")
#         password_d1=self.chrome.find_element_by_id("password_dl")
#         button=self.chrome.find_elements_by_class_name("loginbutton1")
#
#         username_d1.send_keys("17603987065")
#         password_d1.send_keys("123476567")
#         button[0].click()
#
#         text=self.chrome.find_element_by_id("J_usernameTip").text
#         self.assertEqual("账号不存在",text,"内容提示有误")
#     def tearDown(self):
#         sleep(10)
#         self.chrome.close()
# if __name__=='__main__':
#     unittest.main()
import unittest
from time import sleep
from selenium import webdriver
class YouJiuye(unittest.TestCase):
    def setUp(self):
        self.chrome=webdriver.Chrome()
        self.chrome.get("http://xue.ujiuye.com/foreuser/login/")
    def longin(self,username_d,password_d):
        username_dl=self.chrome.find_element_by_id("username_dl")
        password_dl=self.chrome.find_element_by_id("password_dl")
        button=self.chrome.find_elements_by_class_name("loginbutton1")

        username_dl.send_keys(username_d)
        password_dl.send_keys(password_d)
        button[0].click()
        text=self.chrome.find_element_by_id("J_usernameTip").text
        return text
    def test_login_username(self):
        text=self.longin("17603987065","12389766899")
        self.assertEqual("账户不存在",text,"提示内容错误")
    def test_login_password(self):
        text=self.longin("17603987065","1234")
        self.assertEqual("密码应该为6-20之间",text,"密码提示内容错误")
    def tearDown(self):
        sleep(10)
        self.chrome.close()
if __name__=='__main__':
    unittest.main()






