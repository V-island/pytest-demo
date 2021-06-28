import pytest
from data.login_data import LoginData


@pytest.mark.loginTest
class TestLogin(object):
    """登录"""
    login_data = LoginData

    @pytest.mark.parametrize('username, password', login_data.login_success_data)
    def test_login(self, open_url, username, password):
        """登录成功"""
        login_page = open_url[0]
        login_page.login(username, password)
        actual = login_page.get_login_success_account()
        assert '账户概览' in actual, "登录成功, 断言失败"

    @pytest.mark.parametrize('username, password', login_data.login_two_stop_data)
    def test_two_stop_login(self, open_url, username, password):
        """双重验证登录成功"""
        login_page = open_url[0]
        login_page.two_stop_login(username, password)
        actual = login_page.get_login_success_account()
        assert '账户概览' in actual, "登录成功, 断言失败"

    @pytest.mark.parametrize('username, password, expect', login_data.login_verify_data)
    def test_login_verify(self, open_url, username, password, expect):
        """页面输入格式校验"""
        login_page = open_url[0]
        login_page.login(username, password)
        actual = login_page.get_error_verify_text()
        assert actual == expect, "输入格式不正确，断言失败"

    @pytest.mark.parametrize('username, password, expect', login_data.login_fail_data)
    def test_fail(self, open_url, username, password, expect):
        """登录失败"""
        login_page = open_url[0]
        login_page.login(username, password)
        actual = login_page.get_error_text()
        assert actual == expect, "登录失败, 断言失败"


if __name__ == "__main__":
    pytest.main(['-v', 'test_loginCase.py'])
