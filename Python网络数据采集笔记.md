### Python网络数据采集

#### 第一章

##### 网络连接
* ``浏览器层``  `` 网络连接层``
* 浏览器是一个比较年轻的发明，始于1900年的Nexus浏览器
* 网络浏览器：创建信息的数据包，发送他们，然后把获取的数据解释成漂亮的图像、声音、视频、文字。
* 网络浏览器就是代码：而代码是可以分解的，可以分解成许多基本组件，可重写，重用，以及做成我们想要的东西

* 最简单的爬虫代码

```
from urllib.request import urlopen

html = urlopen('https://google.com')
print(html.read())

```
* 我们的Python 程序并没有返回并向服务器请求多个文件的逻辑，他只能读取我们已经请求的单个HTML文件。
* urllib python 标准库，BS4不是标准库 需要自己安装

##### virtualenv
```
$ virtualenv scrapingEvn
$ cd scrapingEnv
$ source bin/activate
$ pip install beautifulsoup4
$ python ...
$ ``from bs4 import BeautifulSoup``
$ 退出scrapingEvn 文件夹 引用bs4 报错
```
##### BeautifulSoup （BS4）

* 安装 
  * mac ``sudo easy_install pip``  ``pip install beautifulsoup4`` 或者 ``pip3 install beautifulsoup4``
  * linux ``sudo apt-get install python-bs4``
  * windows 下载源码``python setup.py install`` 或者 安装win 版本[pip](https://pypi.python.org/pypi/setuptools) 之后 ,``pip install beautifulsoup4``
  
 * 测试安装 ``from bs4 import BeautifulSoup``
 
 * 使用bs4
 ```
 from urllib.request import urlopen
 from bs4 import BeautifulSoup
 html = urlopen('https://google.com')
 bsObj = BeautifulSoup(html.read())
 print(bsObj.h1)
 
 ```
 
