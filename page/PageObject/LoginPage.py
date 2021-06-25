from config.conf import OPEN_CLIENT_URL
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class LoginPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 邮箱或手机号码
    username = do_conf.get_locators_or_account('LoginPageElements', 'userName')
    # 密码输入框
    password = do_conf.get_locators_or_account('LoginPageElements', 'passWord')
    # 登录按钮
    loginBtn = do_conf.get_locators_or_account('LoginPageElements', 'loginBtn')
    # 手机号码/区号
    areaCodeSelect = do_conf.get_locators_or_account('LoginPageElements', 'areaCodeSelect')
    # 登录失败的提示信息
    errorExplain = do_conf.get_locators_or_account('LoginPageElements', 'errorExplain')
    # 登录成功后的用户显示元素
    account = do_conf.get_locators_or_account('HomePageElements', 'account')

    def login(self, username, password):
        """登录流程"""
        self.open_url()
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()

    def open_url(self):
        return self.load_url(OPEN_CLIENT_URL)

    def clear_username(self):
        return self.clear(*LoginPage.username)

    def input_username(self, username):
        self.clear_username()
        return self.send_keys(*LoginPage.username, username)

    def clear_password(self):
        return self.clear(*LoginPage.password)

    def input_password(self, password):
        self.clear_password()
        return self.send_keys(*LoginPage.password, password)

    def click_login_btn(self):
        return self.click(*LoginPage.loginBtn)

    def get_error_text(self):
        return self.get_element_text(*LoginPage.errorExplain)

    def get_login_success_account(self):
        return self.get_element_text(*LoginPage.account)


if __name__ == "__main__":
    pass
