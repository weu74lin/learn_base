# FastAPI

[教程 - 用户指南 - FastAPI](https://fastapi.tiangolo.com/zh/tutorial/)

[FastAPI 安装 | 菜鸟教程](https://www.runoob.com/fastapi/fastapi-install.html)

> > **任务：**

> > 写一个带两个接口的 FastAPI 服务（GET 查询 + POST 提交），用 `uvicorn` 跑起来

主要应用：web应用（依据网络api等获得代码）

API（**Application Programming Interface**）：软件之间进行通信和数据交互的规则和接口，使不同程序能够安全、高效地协作

- 可能包括函数、类、HTTP网络请求
- 主要出现形式：出现在程序语言中（python自带函数）、出现在安装依赖（库的函数）、用了第三方服务以网络形式请求出现
- 目前最通用、使用最广泛的API标准叫作REST API

[GitHub REST API documentation - GitHub Docs](https://docs.github.com/en/rest?apiVersion=2026-03-10)

> > **其它：**[FastAPI 与 Flask：Python Web 两大流行框架综合对比](https://apifox.com/apiskills/fastapi-vs-flask/)

# 知识

## **curl** 命令

是一个强大的命令行工具，用于在 Linux、macOS 和 Windows 系统中传输数据。它支持多种协议（如 HTTP、HTTPS、FTP 等）。

```javascript
curl [options] [URL]
```

- **options**：用于控制 curl 的行为，例如请求方法、头部信息等。
- **URL**：目标地址。

## Cookies和Header

- cookies：网站在每个来访用户身上标记的小标签，省去每次重复登入
- header            （F12）

![image.png](https://resv2.craft.do/user/full/e4c6d501-e82b-4852-84e0-bf7ec38f811e/doc/c81cea23-63cd-41d3-857e-3ec129b74fe7/4b88f1af-c752-4b7c-a7ae-27e81ddf5cf7)

## 并发和并行

- 并发：I/O密集型（等待时间长）时使用
- 并行：CPU密集型（大量计算）时使用

## 异步代码

`async` 和 `await`

`await` 位于操作前（告诉Python 它要等待该操作，此时它可以去做其他事情），想要`await` **生效**则必须在函数`def`前使用`async`

```javascript
async def get_burgers(number: int):
    # 执行一些异步操作来制作汉堡
    return burgers
burgers = await get_burgers(2)
```

协程：只是 `async def` 函数返回的一个非常奇特的东西的称呼

## 请求体

**请求体**是客户端发送给你的 API 的数据。**响应体**是你的 API 发送给客户端的数据。

> 发送数据应使用以下之一：`POST`（最常见）创建数据、`PUT`更新数据、`DELETE` 或 `PATCH`。

> `GET` 查询数据

```javascript
from fastapi import FastAPI
from pydantic import BaseModel #补全、检查
 #创建数据模型：继承BaseModel类
class Item(BaseModel):
    name: str
    description: str | None = None #有默认值，可选
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```

## 路径参数

见执行

## 依赖注入

`Depends` 声明依赖，只能给 `Depends` 传入一个参数。

这个参数必须是类似**函数**的可调用对象。

```javascript
from typing import Annotated #一个变量
from fastapi import Depends, FastAPI

app = FastAPI()

async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
'''async def read_items(commons: dict = Depends(common_parameters)):‘’‘
    return commons

@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
```

## 部署

# 执行

将代码写入py脚本fastap1.py（**::基础::**）：

```javascript
from fastapi import FastAPI
app = FastAPI()
@app.get("/items/{item_id}")#定义一个路径操作装饰器：接收位于其下方的函数并且用它完成一些工作
async def read_item(item_id: int):
    return {"item_id": item_id}
```

然后： `uvicorn fastapi1:app --reload`

之后点击[ http://127.0.0.1:8000/items/foo]( http://127.0.0.1:8000/items/foo) 获得一个JSON界面

**中间经历的步骤：**

1. > 终端执行 uvicorn fastapi1:app --reload

   > → 读入 [fastapi1.py](http://fastapi1.py)，找到 app = FastAPI()

   > → 在本机启动 HTTP 服务，监听 127.0.0.1:8000

2. > 浏览器打开 [http://127.0.0.1:8000/items/foo](http://127.0.0.1:8000/items/foo)

   > → 向「本机 8000 端口」发 GET 请求

   > → 路径是 /items/foo

3. > FastAPI 看路由表

   > → 匹配到 @app.get("/items/{item_id}")

   > → 把路径里的 foo 填进参数 item_id

4. > 执行函数

   > → return {"item_id": item_id}

   > → 变成 JSON：{"item_id":"foo"}

5. > 浏览器显示这个 JSON

`127.0.0.1` = 本机自己；`8000` = 你这个服务占用的端口；`/items/foo` = 请求路径。

另外可以顺手打开文档页：[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)这是 FastAPI 自动生成的交互文档，点一下就能试接口。

?descriptionFromFileType=function+toLocaleUpperCase()+{+[native+code]+}+File&mimeType=application/octet-stream&fileName=FastAPI.md&fileType=undefined&fileExtension=md