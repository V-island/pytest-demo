import pytest
from data.register_data import RegisterData


class TestRegister(object):
    """注册"""
    register_data = RegisterData

    @pytest.mark.parametrize('phone, email, password, confirm, expect', register_data.register_data)
    def test_register(self, open_url, phone, email, password, confirm, expect):
        """注册成功"""
        login_page = open_url[0]
        register_data = open_url[1]
        login_page.click_register()

        register_data.input_phone(phone)
        register_data.click_phone_code_btn()
        phone_code = register_data.get_code_text()

        if expect == phone_code:
            assert expect == phone_code, "用户名已存在, 断言失败"

        register_data.input_phone_code(phone_code)
        register_data.sleep(3)
        register_data.input_email(email)
        register_data.click_email_code_btn()
        register_data.sleep(1)
        email_code = register_data.get_code_text()
        register_data.input_email_code(email_code)
        register_data.input_password(password)
        register_data.input_confirm_password(confirm)
        register_data.click_register_btn()
        actual = register_data.get_error_verify_text()

        register_data.sleep(1)
        register_data.refresh_url()

        assert expect == actual, "注册成功, 断言失败"


if __name__ == "__main__":
    pytest.main(['-v', 'test_registerCase.py'])
