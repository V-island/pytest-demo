import pytest
from selenium import webdriver
from py._xmlgen import html

_driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """当测试失败的时候，自动截图，展示到html报告中"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    # if report.when == 'call' or report.when == "setup":
    #     xfail = hasattr(report, 'wasxfail')
    #     if (report.skipped and xfail) or (report.failed and not xfail):
    #         file_name = report.nodeid.replace("::", "_") + ".png"
    #         screen_img = _capture_screenshot()
    #         if file_name:
    #             html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
    #                 'onclick="window.open(this.src)" align="right"/></div>' % screen_img
    #             extra.append(pytest_html.extras.html(html))
    #     report.extra = extra
    extra.append(pytest_html.extras.text('some string', name='Different title'))
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 设置编码显示中文

def _capture_screenshot():
    """
    截图保存为base64
    :return:
    """
    return _driver.get_screenshot_as_base64()

# def pytest_configure(config):
#     # 添加接口地址与项目名称
#     config._metadata["项目名称"] = "Linux超博客园自动化测试项目v1.0"
#     config._metadata['接口地址'] = 'https://www.cnblogs.com/linuxchao/'
#     # 删除Java_Home
#     config._metadata.pop("JAVA_HOME")

# @pytest.mark.optionalhook
# def pytest_html_results_summary(prefix):
#     prefix.extend([html.p("所属部门: xx测试中心")])
#     prefix.extend([html.p("测试人员: Linux超")])

@pytest.fixture(scope='module')
def driver():
    global _driver
    print('------------open browser------------')
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    yield _driver
    print('------------close browser------------')
    _driver.quit()
