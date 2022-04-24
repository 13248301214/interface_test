# 单元测试：就是定义一个函数或者方法
"""
-- 测的是什么功能？
然后选择是用工具还是用框架
-- 断言 -- 测试  -- 返回的结果 期望的结果是否一致？

接下来看怎么去测

-- 运行测试用例
1、直接点击绿色按钮 运行 测试用例 方式执行
2、命令行的方式执行
直接输入  pytest   目录下  符合测试用例规则的  全部执行
assert 返回True或False(证明断言失败)

--- 选择?        指定的py文件执行  python test_demo.py  pytest tests_demo.py  test_demo2.py
--- 指定测试用例？ pytest -k login
--- print(name) pytest -s
--- 如果同时测登录和注册  添加标签 @


--- 数据驱动  -- （拿着不同的数据 -- 相同的功能）
  一个参数？
    -- 1 -- 参数名字
    -- 2 -- 参数值
  两个参数？

--- 注册  给10位数字  1890000000  带有特殊字符 190  884333   注册过的  -- 注册


课堂上不建议大家跟着练习，尤其对于没接触过新知识，你可能听到一句，后面说的啥就不知道了，视频回放和笔记都有，你们
需要的化稍后可以添加助教老师微信

如果感觉跟起来比较困难，需要什么资料，可以找助教老师


# 接下来测一个真实的天气预报接口案例
# 首先问他  接口文档  url  method res_data params
https://tianqiapi.com/
https://tianqiapi.com/index/doc  api文档


"""
import pytest
import requests


# 方法
# def add(x, y):
#     """
#     求两个数相加
#     :param x:
#     :param y:
#     :return:
#     """
#     return x + y

def add(x):
    return x


def add2(x, y):
    return x + y

# 方法
def register():
    print("用户注册")


# 方法
def login():
    print("用户登录")

# 测试用例
# 数据驱动 -- 装饰器
# 调用处理好数据
# get_data = [1, 2, 3, 3, 5]
# 一个参数
# @pytest.mark.parametrize("x, y", get_data)
# 两个参数
@pytest.mark.parametrize("name,pwd", [('admin','123456'),('user','123456')])
def test_01(name,pwd):
    print(name)
    print(pwd)
    # 这里我断言调用方法 add返回结果是否等于5
    # assert add(1 ,2) == 5
    # assert add(x) == 5
    # assert add2(x, y) == 5



# 测试用例
# def test_02():
#     assert 1 == 1

@pytest.mark.parametrize("city", ["郑州", "上海", "北京"])
def test_03(city):
    # url = 'https://tianqiapi.com/api?appid=35767487&appsecret=K1QBqU0y&version=v61&city=上海'
    url = "https://tianqiapi.com/api?appid=35767487&appsecret=K1QBqU0y&version=v61&city=%s"%city
    res = requests.get(url=url)
    # print(res.json()['air_tips'])
    # 断言 -- 响应  期望的结果和实际结果对比
    assert res.json()['city'] == city




"""
1.之前做功能测试   脚本  框架 入手  用的多了  工具也不想用了
2.之前做开发，技术没问题，重点放在基础理论方法  逐步把这块系统化下来
"""


