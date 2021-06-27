from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class HomePage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    


if __name__ == '__main__':
    pass
