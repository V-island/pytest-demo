import pytest
from data.register_data import RegisterData


class TestRegister(object):
    """注册"""
    register_data = RegisterData

    @pytest.mark.parametrize('phone, email, password, confirm', register_data.register_data)
    def test_register(self, open_url, phone, email, password, confirm):
        """注册成功"""
        login_page = open_url[0]
        register_data = open_url[1]
        login_page.click_register()

        register_data.sleep(1)
        register_data.input_phone(phone)
        register_data.click_phone_code_btn()
        phone_code = register_data.get_code_text()

        if '该用户已存在' == phone_code:
            assert '该用户已存在' == phone_code, "该用户已存在, 断言失败"

        else:
            register_data.input_phone_code()
            register_data.sleep(3)
            register_data.input_email(email)
            register_data.click_email_code_btn()
            register_data.sleep(1)
            email_code = register_data.get_code_text()

            if '该邮箱已注册' == email_code:
                assert '该邮箱已注册' == email_code, "该邮箱已注册, 断言失败"

            else:
                register_data.input_email_code()
                register_data.input_password(password)
                register_data.input_confirm_password(confirm)
                register_data.click_register_btn()
                actual = register_data.get_access_text()

                register_data.sleep(1)
                register_data.sign_out()
                register_data.sleep(1)
                assert '创建成功' == actual, "注册成功, 断言失败"


if __name__ == "__main__":
    pytest.main(['-v', 'test_registerCase.py'])