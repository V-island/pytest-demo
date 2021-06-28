class LoginData(object):
    """用户登录测试数据"""

    login_success_data = [
        (
            "13511113333",
            "Asd123456"
        )
    ]

    login_two_stop_data = [
        (
            "13511112222",
            "Asd123456"
        )
    ]

    login_verify_data = [
        (
            "",
            "Asd123456",
            "请输入登录的邮箱或手机号码"
        ),
        (
            "13511113333",
            "",
            "请输入您的密码"
        )
    ]

    login_fail_data = [
        (
            "13511113334",
            "123456",
            "用户不存在"
        ),
        (
            "13511113333",
            "123456",
            "登录密码错误"
        )
    ]


if __name__ == '__main__':
    pass
