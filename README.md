安装web环境

一、

```
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
$ exec $SHELL -l    

二、
安装包
$ sudo apt-get install libc6-dev gcc
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm

三、
$ pyenv install 3.7.3 -v

四、更新pyenv的数据库
    pyenv rehash
    
五、选中3.7.3(pyenv数据库中存在的版本)作为默认版本  
    pyenv global 3.7.3
    pyenv versions版本查看
六(下一个，这跳过)、
使用pyenv+virtualenv创建虚拟环境
1.使用pip安装virtualenv
    pip install virtualenv
2.创建你的python虚拟环境(3.6.4是你pyenv数据库中存在的版本,env36是你虚拟环境的名字,可以任意起)
    pyenv virtualenv 3.6.4 env36
3.切换到你的虚拟环境
    pyenv activate env36
    如果命令行中有(env36),如(env36) yfx@bo:~$,说明你处于env36的虚拟环境中
4.退出虚拟环境
    pyenv deactivate
    
七、
1.git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
2.$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
3.$ source ~/.bashrc
4.ubuntu@VM-0-9-ubuntu:~$ mkdir MyPython
ubuntu@VM-0-9-ubuntu:~$ cd MyPython/
ubuntu@VM-0-9-ubuntu:~/MyPython$ ll
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Oct 30 19:06 ./
drwxr-xr-x 8 ubuntu ubuntu 4096 Oct 30 19:06 ../
5.pyenv virtualenv 3.6.3 env363
cd '/home/ubuntu/.pyenv'

6.pyenv deactivate

八、
1.安装mysql
root@coding:~# apt-get update
root@coding:~# apt-get install mysql-server
2.
root@coding:~# apt-get install nginx

九、数据库路径
(classstu) ubuntu@VM-0-9-ubuntu:~/.pyenv/versions/3.7.3/envs/classstu/lib/python3.7/site-packages/django/db/backends/mysql
```