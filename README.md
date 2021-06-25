# PayClientAutoTest


#### 安装教程

1.  pip install -r requirements.txt
2.  python RunTestCase.py

##### 单虚拟环境的情况 生成requirements.txt

1.  pip freeze > requirements.txt

##### 使用 pipreqs 生成requirements.txt
1.  pip install pipreqs
2.  pipreqs . --encoding=utf8 --force


#### 环境需求

1.python3.x
2.pip install selenium
3.pip install pytest-rerunfailures
4.pip install pytest-html