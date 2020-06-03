import allure
import pytest


class TestAction:

    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.skipif(True, reason='')
    @allure.step(title='用户名')
    def test_username(self):
        print('test_username')
        assert True

    # @pytest.mark.skipif(True, reason='')
    @allure.step(title='密码')
    def test_pwd(self):
        print('test_pwd')
        assert False

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title='测试登录脚本')
    def test_login(self):
        allure.attach('输入内容：chenxiaonan', '输入用户名')
        print('输入用户名')

        allure.attach('输入内容：123456', '输入密码')
        print('输入密码')
        assert True
