import pytest
from data.register_data import RegisterData


class TestRegister(object):
    """注册"""
    register_data = RegisterData

    @pytest.mark.parametrize('username, email, password, confirm', register_data.register_data)
    def test_register(self, open_url, username, email, password, confirm):
        """注册成功"""
        login_page = open_url[0]
        register_data = open_url[1]
        login_page.click_register()
        register_data.register(username, email, password, confirm)
        actual = register_data.get_login_success_account()
        assert '账户概览' in actual, "注册成功且自动登录成功, 断言失败"


if __name__ == "__main__":
    pytest.main(['-v', 'test_registerCase.py'])
