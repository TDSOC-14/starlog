# starlog
星笔记-星辰14班在线笔记
## 如何开始开发？
新建一个文件夹，然后在里面下载此项目。
然后在终端中输入：
### 创建虚拟环境
```
python -m venv ll_env 
```
（注意在Ubuntu等Linux发行版上可能是python3）
### 启用虚拟环境
Windows
```
ll_env\Scripts\activate
```
Linux
```bash
source ll_env/bin/activate
```
### 下载Django（请在虚拟环境下）
```
pip install django
```
### 开启服务器
```
python manage.py runserver
```
注意请在虚拟环境下开启。
然后打开浏览器，在搜索框输入 http://localhost:8000 （Django默认使用8000端口）


