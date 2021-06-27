class LoginData(object):
    """用户登录测试数据"""

    login_success_data = [
        (
            "13511113333",
            "Asd123456"
        ),
        (
            "13511112222",
            "Asd123456"
        )
    ]

    login_fail_data = [
        (
            "1351113333",
            "",
            "请输入密码"
        ),
        (
            "",
            "123456",
            "请输入帐号"
        ),
        (
            "linux",
            "xiaochao",
            "帐号或密码错误"
        )
    ]


if __name__ == '__main__':
    pass
