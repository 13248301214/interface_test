"""
1、什么是框架？

半成品，别人封装好的 内容，我们可以直接拿过来使用

常用的框架
pytest和unitest

对比  --unitest(单元测试)  pytest
    unitest -- 不支持支持重跑
            -- 参数化，第三方库
            -- 生成测试报告 HTMLtestrunner --
    pytest  -- 支持失败 重新执行  --插件
            -- 参数化 -- 自带的装饰器
            -- allure -- 强大  生成美观的测试报告

2、测试项目
test_case 测试用例
test_data 数据分离  数据驱动
config    项目配置
common    别人封装好的，项目里面提取一些公共方法
report    测试报告
log       测试日志

这里我们创建包都是以test开头
pytest-- 测试用例  （文件命名--符合）
文件都要以test_开头或_test结尾，类名Test开头，这里统一以test_开头
"""
import pytest
import requests


def add(x):
    return x


def test_01():
    assert 1 == 1


get_data = [1, 2, 3, 3, 5]
@pytest.mark.parametrize("x", get_data)
def test_02(x):
    assert add(x) == 5
#
# @pytest.mark.smoke
# @pytest.mark.parametrize("name,pwd", [('admin','123456'),('user','123456')])
# def test_03(name,pwd):
#     print(name)
    # print(pwd)

@pytest.mark.parametrize("city", ["上海"])
def test_03(city):
    # url = 'https://tianqiapi.com/api?appid=35767487&appsecret=K1QBqU0y&version=v61&city=上海'
    url = "https://tianqiapi.com/api?appid=35767487&appsecret=K1QBqU0y&version=v61&city=%s"%city
    res = requests.get(url=url)
    # print(res.json())
    # print(res.json()['air_tips'])
    # 断言 -- 响应  期望的结果和实际结果对比
    assert res.json()['city'] == city


if __name__ == "__main__":
    pytest.main()
