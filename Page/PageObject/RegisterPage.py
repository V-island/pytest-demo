from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class RegisterPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 访问登录页
    visitLoginBtn = do_conf.get_locators_or_account('RegisterPageElements', 'visitLoginBtn')
    # 手机号码
    phone = do_conf.get_locators_or_account('RegisterPageElements', 'phone')
    # 手机验证码
    phoneCode = do_conf.get_locators_or_account('RegisterPageElements', 'phoneCode')
    # 获取手机验证码
    phoneCodeBtn = do_conf.get_locators_or_account('RegisterPageElements', 'phoneCodeBtn')
    # 邮箱
    email = do_conf.get_locators_or_account('RegisterPageElements', 'email')
    # 邮箱验证码
    emailCode = do_conf.get_locators_or_account('RegisterPageElements', 'emailCode')
    # 获取邮箱验证码
    emailCodeBtn = do_conf.get_locators_or_account('RegisterPageElements', 'emailCodeBtn')
    # 密码
    passWord = do_conf.get_locators_or_account('RegisterPageElements', 'passWord')
    # 确认密码
    confirmPassWord = do_conf.get_locators_or_account('RegisterPageElements', 'confirmPassWord')
    # 注册按钮
    registerBtn = do_conf.get_locators_or_account('RegisterPageElements', 'registerBtn')
    # 获取验证码消息提示
    getCodeText = do_conf.get_locators_or_account('RegisterPageElements', 'getCodeText')

    # 校验失败提示信息
    errorVerify = do_conf.get_locators_or_account('RegisterPageElements', 'errorVerify')
    # 登录失败提示信息
    errorExplain = do_conf.get_locators_or_account('RegisterPageElements', 'errorExplain')

    # 注册完成自动登录
    accessBtn = do_conf.get_locators_or_account('HomePageElements', 'accessBtn')
    accessExplain = do_conf.get_locators_or_account('HomePageElements', 'accessExplain')
    personalCenterMenu = do_conf.get_locators_or_account('HomePageElements', 'personalCenterMenu')
    signOutItem = do_conf.get_locators_or_account('HomePageElements', 'signOutItem')

    # 访问登录页
    def click_login(self):
        return self.click(*RegisterPage.visitLoginBtn)

    # 获取验证码消息提示 注:测试环境验证码以消息提示返回
    def get_code_text(self):
        return self.get_element_text(*RegisterPage.getCodeText)

    # 手机号
    def input_phone(self, phone):
        self.clear(*RegisterPage.phone)
        return self.send_keys(*RegisterPage.phone, phone)

    # 获取手机验证码
    def click_phone_code_btn(self):
        return self.click(*RegisterPage.phoneCodeBtn)

    # 手机验证码
    def input_phone_code(self, code):
        self.clear(*RegisterPage.phoneCode)
        return self.send_keys(*RegisterPage.phoneCode, code)

    # 邮箱
    def input_email(self, email):
        self.clear(*RegisterPage.email)
        return self.send_keys(*RegisterPage.email, email)

    # 获取邮箱验证码
    def click_email_code_btn(self):
        return self.click(*RegisterPage.emailCodeBtn)

    # 邮箱验证码
    def input_email_code(self, code):
        self.clear(*RegisterPage.emailCode)
        return self.send_keys(*RegisterPage.emailCode, code)

    # 密码
    def input_password(self, password):
        self.clear(*RegisterPage.passWord)
        return self.send_keys(*RegisterPage.passWord, password)

    # 确认密码
    def input_confirm_password(self, password):
        self.clear(*RegisterPage.confirmPassWord)
        return self.send_keys(*RegisterPage.confirmPassWord, password)

    # 注册按钮
    def click_register_btn(self):
        return self.click(*RegisterPage.registerBtn)

    # 校验格式提示信息
    def get_error_verify_text(self):
        return self.get_element_text(*RegisterPage.errorVerify)

    # 登录失败提示信息
    def get_error_text(self):
        return self.get_element_text(*RegisterPage.errorExplain)

    # 登录信息
    def get_access_text(self):
        return self.get_element_text(*RegisterPage.accessExplain)

    # 退出登录
    def sign_out(self):
        self.click(*RegisterPage.accessBtn)
        self.move(*RegisterPage.personalCenterMenu)
        return self.click(*RegisterPage.signOutItem)


if __name__ == "__main__":
    pass
