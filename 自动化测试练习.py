import unittest
# a=1
# assert a,"a is false"
# print(a)
# a=1
# if not a:
#     raise AssertionError('a is false')
# print(a)
#unittest例子
# import unittest
# #unittest的是使用方法
# class OurTest(unittest.TestCase):
#     #继承编写测试类的基础
#     def steUp(self):
#         pass
#         #类似于init方法，在测试执行之初制动执行，通常用来测试数据的准备
#     def test_add(self):
#         pass
#         #具体测试的方法，使用testcase编写具体测试的方法，函数名称必须以
#         #test开头，函数当中的内容是获取预期值，和运行结果值，通过2个值的比较
#     def tearDown(self):
#         pass
#         #类似del方法，用来回收测试环境
# if __name__=='__main__':
#     unittest.main()
import unittest
class Ourtest(unittest.TestCase):
    def setUp(self):
        self.a=1
        self.b=1
        self.result=3
    def test_add(self):
        run_result=self.a+self.b
        self.assertEqual(run_result,self.result,'self.a+self.b不等于3')
    def tearDown(self):
        pass
if __name__=='__main__':
    unittest.main()





