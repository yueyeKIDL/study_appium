import allure
import pytest

from base.base_driver import Base


class TestAction:

    def setup_class(self):
        self.driver = Base().driver

    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.skipif(True, reason='')
    @allure.step(title='用户名')
    def test_username(self):
        print('test_username')
        assert True

    @allure.step(title='密码')
    def test_pwd(self):
        allure.attach('输入内容：666666', '输入密码')

        print('test_pwd')
        assert False

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title='测试登录脚本')
    def test_login(self):
        allure.attach('输入内容：yueyeKIDL', '输入用户名')
        print('输入用户名')

        allure.attach('输入内容：123456', '输入密码')
        print('输入密码')
        assert True

    # @allure.step(title='测试截图上传到报告')
    def test_upload_screenshots_to_report(self):
        file_path = './screen/report_screen_shot.png'
        self.driver.get_screenshot_as_file(file_path)
        with open(file_path, 'rb') as f:
            allure.attach('上传截图', f.read(), allure.attachment_type.PNG)
        assert True
