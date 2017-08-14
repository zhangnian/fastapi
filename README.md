# fastapi
基于flask的快速开发Web API的框架

### 安装
```pip install -r requirments.txt```

### 集成的第三方组件
#### Sentry
在配置文件中可以控制是否开启sentry功能，如果开启，当程序出现异常时会将异常信息上报至配置文件中指定的sentry server。

#### flask_sqlalchemy
sqlalchemy的flask扩展

#### flask_marshmallow
对象的序列化/反序列化库，用于实现db.Model对象和JSON之间的快速映射

#### Redis
在utils包中简单封装了一个全局的redis客户端，redis的服务器配置从配置文件中读取


### 扩展的功能
- 使用flask blueprint对项目进行模块化划分
- 封装日志组件，按照每天进行日志滚动

### 快速开始
*TODO*
