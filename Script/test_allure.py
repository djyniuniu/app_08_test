import allure,pytest

class Test_Allure(object):
    @allure.step(title='登录')
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_001(self):
        allure.attach('描述','输入用户名')
        allure.attach('描述', '输入密码')
        allure.attach('描述', '点击登录')
        assert 0

    @allure.step(title='注册')
    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_002(self):
        allure.attach('描述','点击注册')
        allure.attach('注册','注册成功')
        assert 1