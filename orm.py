# import pymysql
#
# class Field(object):
#     def __init__(self,name,column_type):
#         self.name = name
#         self.column_type = column_type
#     def __str__(self):
#         return "<%s:%s>"%(self.name,self.column_type)
#
# class StringField(Field):
#     def __init__(self,name,column_type):
#         super(StringField,self).__init__(name,column_type)
#         self.name=name
#         self.column_type='varchar(100)'
#
# class IntegerField(Field):
#     def __init__(self,name):
#         super(IntegerField,self).__init__(name,"int")
#
# class ModelMetaClass(type):
#     def __new__(cls, name,bases,attrs):
#         '''
#         :param name: 类的名称
#         :param bases: 类的继承
#         :param attrs:  类的属性
#         :return:
#         '''
#         if name == "Model":
#             return type.__new__(cls,name,bases,attrs)
#         mapping = dict() #空字典
#         for k,v in attrs.items(): #遍历属性
#             if isinstance(v,Field): #判断属性是否Field的实例
#                 mapping[k] = v #添加到mapping当中
#         for k in mapping.keys(): #返回所有键
#             attrs.pop(k) #从属性当中删除
#         attrs["__mapping__"] = mapping  #设定__mapping__属性来保存字段
#         attrs["__table__"] = name
#         return type.__new__(cls,name,bases,attrs)
#
# class Model(dict,metaclass = ModelMetaClass):
#     def __init__(self,**kwargs):
#         self.db = pymysql.connect(
#             host = "localhost",
#             user = "root",
#             password = "123",
#             database = "test"
#         )
#         self.cursor = self.db.cursor()
#         super(Model,self).__init__(**kwargs)
#
#     def __getattr__(self, key):
#         return self[key]
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#     def save(self):
#         fields = [] #空列表用来存储字段
#         args = [] #空列表用来存储字段的值
#         for k,v in self.__mapping__.items():
#             fields.append(v.name)
#             args.append(getattr(self,k,None))
#         print(fields)
#         sql = "insert into %s(%s) values (%s)"%(
#             self.__table__,
#             ",".join(fields),
#             ",".join([repr(str(i)) for i in args]
#                )) #sql拼接
#         self.cursor.execute(sql)
#         print(sql)
#     def __del__(self):
#         '''
#         回收内存
#         '''
#         self.db.commit()
#         self.cursor.close()
#         self.db.close()
#
# class Student(Model):
#     name = StringField("name",'num')
#     room_id = IntegerField("room_id")
#
# u = Student(name = "老边",room_id = 18)
# u.save()
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
#创建连接实例
db = sqlalchemy.create_engine("mysql+pymysql://root:123@localhost/sqlalchemydb")
#"数据库类型+数据库模块://用户名:密码@主机/库名"
#定义表
    #定义一个元类的继承类
base = declarative_base(db)

    #开始定义表
class User(base):
    __tablename__ = "user"
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))

if __name__ == "__main__":
    base.metadata.create_all(db)


#进行增删改查
#类似于pymysql 的游标 cursor
from sqlalchemy.orm import sessionmaker

#绑定连接
cursor = sessionmaker(bind=db) #得到的时一个类

session = cursor() #实例化

# 增
user = User(
    id = 1,
    name = "老边"
)
session.add(user)
session.commit()
session.add_all([
    User(id = 2, name = "老赵"),
    User(id = 3, name = "老李")
])
session.commit()
#查
all_data = session.query(User).all() #查所有
print(all_data) #得到对象
for data in all_data:
    print("id:%s__name:%s"%(data.id,data.name))

many_data = session.query(User).filter_by(id = 1) #查多条
data, = many_data
print("id:%s__name:%s" % (data.id, data.name))
for data in many_data:
    print("id:%s__name:%s"%(data.id,data.name))

#data = session.query(User).get(ident=3) #查一条，只能以主键查
#print("id:%s__name:%s" % (data.id, data.name))

#删除
    #先查询一条
# data = session.query(User).get(ident=3)
#     #然后删除
# session.delete(data)
#     #然后提交操作
# session.commit()
#改
    # 先查询一条
# data = session.query(User).get(ident=2)
#     #然后删除
# data.name = "老李"
#     #然后提交操作
# session.commit()
