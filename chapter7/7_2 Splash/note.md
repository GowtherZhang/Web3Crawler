# Splash 的使用
Splash 是一个JavaScript 渲染服务。他是一个带有HTTP API 的轻量浏览器，还对接了 python 中的 Twisted 库和 QT 库。同时包括以下功能：
* 异步处理多个网页的渲染过程
* 获取渲染后的页面的源代码或截图
* 通过关闭图片渲染或者使用 Adblock 规则来加快页面渲染的速度
* 执行特定的 JavaScript 脚本
* 通过 Lua 脚本 来控制页面渲染的过程

# 安装
Splash 使用 Docker 安装，运行在本地的 8050 端口

# Splash 的属性
* args 属性
  * 获取页面加载时的参数，如请求 URL 等
  * splash 支持将 main 方法的第二个参数直接设置为 args,以下两段代码等价
```lua
funtion main(splash)
    local url = splash.args.url
end 

funtion main(splash)
    local url = args.url
end 
```

* js_enabled 属性
  Splash 执行 Java Script 的开关，默认为 true，一般不动它。如下面这段脚本如果设置为false，就会报错。
```lua
function main(splash, args)
  splash:go("https://www.baidu.com")
  splash.js_enabled = false
  local title = splash:evaljs("document.title")
  return {title=title}
end
```

* resource_timeout 属性
设置加载的超时时间，如果设置为 0 或 nil ，代表不检测超时;如下面这一段，0.1 秒之内没有响应就会报错。适合在网页加载速度较慢的情况下设置，如果超时，直接抛出异常即可。
```lua
function main(splash)
    splash.resource_timeout = 0.1
    assert(splash:go('https://www.taobao.com'))
    return splash:png()
end
```

* images_enabled 属性
设置是都加载图片，默认加载，可以节省流量并提高网页加载速度，但是禁用图片加载可能会影响 JavaScript 渲染。
Splash 使用了缓存，如果之前加载过的网页图片，即使你后面禁用了，再重新加载的话还会出来，重启即可。

* plugins_enabled 
控制浏览器插件是否开启，默认不开启。

* scroll_position
控制页面上下或者所有滚动，如 splash.scroll_positon{x=100,y=200},表示向由滚动 100，向左滚动 200。

# Splash 的方法
* go 方法
用来请求某个链接，可以模拟 get 和 post 请求，同时支持传入请求头、表单等数据。
如以下脚本，模拟了一个 post 请求，并传入了一个post的表单数据，如果成功就返回页面的源代码。
```lua
function main(splash, args)
  local ok, reason = splash:go{url="http://httpbin.org/post",http_method="post",body="name=Germey"}
  if ok then
    return splash:html()
  end
end
  ```

* wait 方法
  控制页面的等待时间，有三个参数：
  * time,等待的秒数，
  * cancel_on_redirect, 可选参数，如果发生重定向就停止等待，返回重定向的结果
  * cancel_on_error, 可选参数，如果发生错误就停止等待。
  以下代码可以实现访问淘宝并等待2秒，随后返回源代码
  ```lua
  function main(splash)
	splash:go("http://taobao.com")
	splash:wait(2)
	return {html=splash:html()}
    end
  ```

* jsfunc 方法
  直接调用 JavaScript 定义的方法，调用的方法需要使用双括号包围。
如以下脚本，用来记算页面中 div 节点的个数
```lua
function main(splash, args)
  local get_div_count = splash:jsfunc([[function(){
    var body = document.body;
    var divs = body.getElementsByTagName('div');
    return divs.length;
  }]])
  splash:go("https://www.baidu.com")
  return ("There are % s DIVs"):format(get_div_count())
end
```
* evaljs 方法
  执行 JavaScript 代码，并返回最后一条 JacaScript 语句的返回结果。
  比如以下脚本可以用来获取页面的标题
```lua
local title = splash:evaljs("document.title")
```
* runjs 方法
  与 evaljs 方法类似，但是更偏向于执行某些动作或者声明某些方法。
  如以下脚本，先使用 runjs 声明了一个 JavaScript 定义的方法，然后通过 evljs 方法来调用得到的结果，
```lua
function main(splash, args)
  splash:go("http://baidu.com")
  splash:runjs("foo = function(){return 'bar'}")
  local result = splash:evaljs("foo()")
  return result
 end
```

* autoload 方法
设置每个页面访问时自动加载的对象，负责加载 JavaScript 代码或者库，要执行操作的话，需要调用 evaljs 或者 runjs 方法。
如以下代码，调用 autoload 方法声明了一个 JavaScript 方法，然后通过 evalhjs 来执行这个方法。
```lua
function main(splash, args)
  splash:autoload([[function get_document_title(){return document.title;}
    ]])
  splash:go("https://www.baidu.com")
  return splash:evaljs("get_document_title()")
 end

```
* html 方法
  用来获取网页的源代码，示例如下：
```lua
function main(splash, args)
  splash:go("https://httpbin.org/get")
  return splash:html()
end
```
* png / jpeg
  此方法可以用来获取 PNG/jpeg 格式的网页截图
```lua
function main(splash, args)
  splash:go("https://taobao.com")
  return splash:png()
end
```
* har 方法
  用来显示页面加载过程中每个请求的记录详情
```lua
function main(splash, args)
  splash:go("https://www.baidu.com")
  return splash:har()
end
```
* url 方法
  此方法可以获取当前正在访问的 url,示例如下：
```lua
function main(splash, args)
  splash:go("https://taobao.com")
  return splash:url()
end
```

* set_user_agent
  用来设置浏览器的 User-Agent,示例如下：
```lua
function main(splash, args)
  splash:set_user_agent('Splash')
  splash:go("http://httpbin.org/get")
  return splash:html()
end
```
返回结果如下,其中 User-Agent 已经被设置
```html
<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">{
  "args": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "en,*", 
    "Host": "httpbin.org", 
    "User-Agent": "Splash", 
    "X-Amzn-Trace-Id": "Root=1-6551d1e6-0203b4844ec4e1e51d75a197"
  }, 
  "origin": "167.71.210.86", 
  "url": "http://httpbin.org/get"
}
</pre></body></html>
```

* set_custom_heads()
  用来设置请求头，包含了 set_user_agent() 方法的功能。
示例如下：
```lua
function main(splash, args)
  splash:set_custom_headers({['User-Agent']="Splash",
      ["Site"] = "Splash"})
  splash:go("http://httpbin.org/get")
  return splash:html()
end
```

返回结果如下：
```html
<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">{
  "args": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "en,*", 
    "Host": "httpbin.org", 
    "Site": "Splash", 
    "User-Agent": "Splash", 
    "X-Amzn-Trace-Id": "Root=1-6551d3d9-2355c97c451ad12b49d09e8f"
  }, 
  "origin": "167.71.210.86", 
  "url": "http://httpbin.org/get"
}
</pre></body></html>
```

* select 方法
  可以选中符合条件的第一个节点，参数是 CSS 选择器，示例如下,运行结果的截图中显示已经成功填写输入框。
```lua
function main(splash, args)
  splash:go("http://baidu.com")
  input = splash:select('#kw')
  input:send_text('Splash')
  splash:wait(3)
  return splash:png()
end
```
* select_all 方法
  可以选中所有符合条件的节点，参数是 CSS 选择器。示例如下，选中了节点的正文内容，然后遍历所有节点，将其中的文本获取下来。
```lua
function main(splash)
  local treat = require('treat')
  assert(splash:go("https://quotes.toscrape.com/"))
  assert(splash:wait(0.5))
  local texts = splash:select_all('.quote .text')
  local results = {}
  for index, text in ipairs(texts) do
    results[index] = text.node.innerHTML
  end
  return treat.as_array(results)
end
```

* mouse_click
模拟鼠标点击的操作，传入的参数为坐标值x, y,也可以选中某个节点调用此方法，示例如下：
```lua
function main(splash)
  splash:go("https://www.baidu.com/")
  input = splash:select("#kw")
  input:send_text('Splash')
  submit = splash:select('#su')
  submit:mouse_click()
  splash:wait(3)
  return splash:png()
end
```

# Splash API 的调用
Splash 提供了一些 HTTP API 接口，我们只需要请求这些接口并传递相应的参数就可以获取页面渲染后的结果。
* render.html
  用于获取 JavaScript 渲染的页面的 HTML 代码，接口地址就是 Splash 的运行地址加上此接口名称。示例如下,可以输出百度页面渲染后的源代码。
```python
import requests
url = 'http://localhost:8050/render.html?url=https://www.baidu.com'
response = requests.get(url)
print(response.text)
```

* render.png / render.jpeg
  用于获取网页截图，可以通过 width 和 height 来控制截图大小。示例如下：
```python
url = 'http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
response = requests.get(url)
with open('taobao.png', 'wb') as f:
    f.write(response.content)
```

* execute
  使用此接口实现与 Lua 脚本的对接，html 与 png 等接口无法实现一些交互操作，需要execute 接口。
  ```python
  import requests
from urllib.parse import quote

lua = '''
function main(splash)
    return 'hello'
end
'''

url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)
  ```