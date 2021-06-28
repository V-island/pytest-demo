from config.conf import OPEN_CLIENT_URL
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class LoginPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 访问注册页
    visitRegisterBtn = do_conf.get_locators_or_account('LoginPageElements', 'visitRegisterBtn')
    # 邮箱或手机号码
    username = do_conf.get_locators_or_account('LoginPageElements', 'userName')
    # 密码输入框
    password = do_conf.get_locators_or_account('LoginPageElements', 'passWord')
    # 登录按钮
    loginBtn = do_conf.get_locators_or_account('LoginPageElements', 'loginBtn')

    # 手机号码/区号
    areaCodeSelect = do_conf.get_locators_or_account('LoginPageElements', 'areaCodeSelect')
    # 密码显示隐藏切换
    passWordSuffix = do_conf.get_locators_or_account('LoginPageElements', 'passWordSuffix')

    # 校验失败提示信息
    errorVerify = do_conf.get_locators_or_account('LoginPageElements', 'errorVerify')
    # 登录失败提示信息
    errorExplain = do_conf.get_locators_or_account('LoginPageElements', 'errorExplain')

    # 双重验证获取验证码
    verifyCodeBtn = do_conf.get_locators_or_account('LoginPageElements', 'verifyCodeBtn')
    # 双重验证输入验证码
    verifyCode = do_conf.get_locators_or_account('LoginPageElements', 'verifyCode')
    # 获取验证码
    getVerifyCode = do_conf.get_locators_or_account('LoginPageElements', 'getVerifyCode')

    # 登录成功后进入菜单
    navMenu = do_conf.get_locators_or_account('HomePageElements', 'navMenu')
    signOutBtn = do_conf.get_locators_or_account('HomePageElements', 'signOutItem')

    # 统一登录入口
    def login(self, username, password):
        """登录流程"""
        self.open_url()
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()

    # 双重登录入口
    def two_stop_login(self, username, password):
        """双重登录流程"""
        self.open_url()
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()

        if self.is_element_exist(*LoginPage.verifyCodeBtn):
            self.click_verify_code_btn()
            code = self.get_verify_code()
            self.input_verify_code(code)

    # 访问页面
    def open_url(self):
        return self.load_url(OPEN_CLIENT_URL)

    # 访问注册页
    def click_register(self):
        self.open_url()
        return self.click(*LoginPage.visitRegisterBtn)

    def clear_username(self):
        return self.clear(*LoginPage.username)

    # 登录邮箱/手机号
    def input_username(self, username):
        self.clear_username()
        return self.send_keys(*LoginPage.username, username)

    def clear_password(self):
        return self.clear(*LoginPage.password)

    # 登录密码
    def input_password(self, password):
        self.clear_password()
        return self.send_keys(*LoginPage.password, password)

    # 登录按钮
    def click_login_btn(self):
        return self.click(*LoginPage.loginBtn)

    # 获取验证码按钮
    def click_verify_code_btn(self):
        return self.click(*LoginPage.verifyCodeBtn)

    def get_verify_code(self):
        return self.get_element_text(*LoginPage.getVerifyCode)

    def clear_verify_code(self):
        return self.clear(*LoginPage.verifyCode)

    # 写入验证码
    def input_verify_code(self, code):
        self.clear_verify_code()
        return self.send_keys(*LoginPage.verifyCode, code)

    # 校验格式提示信息
    def get_error_verify_text(self):
        return self.get_element_text(*LoginPage.errorVerify)

    # 登录失败提示信息
    def get_error_text(self):
        return self.get_element_text(*LoginPage.errorExplain)

    # 登录成功后验证跳转
    def get_login_success_account(self):
        return self.get_element_text(*LoginPage.navMenu)

    # 退出当前登录
    def click_sign_out_btn(self):
        return self.click(*LoginPage.signOutBtn)


if __name__ == "__main__":
    pass
