# Time node for ChatGPT-Mirai-QQ-Bot

向工作流中添加当前日期和时间的插件，以便配合搜索使用


## 使用

在 chatgpt-mirai-qq-bot的web_ui中配置  
使用示例请参考 [web_search/example/roleplayWithWebSearch.yml](web_search/example/roleplayWithWebSearch.yaml)    
工作流请参考 [示例图片](web_search/example/workflow.png)

## 新增功能

### TimeBlock

新增了一个 `TimeBlock`，可以获取指定时区或服务器本地时间。

#### 使用示例

在 `C_time/example/time_example.yaml` 中提供了一个示例工作流，展示了如何使用 `TimeBlock`。

```yaml
name: 获取时间示例
blocks:
  - type: time_block
    name: get_time
    params:
      timezone: "Asia/Shanghai"
    position:
      x: 100
      y: 100
    connected_to:
      - target: print_time
        mapping:
          from: current_time
          to: time
  - type: internal:print
    name: print_time
    params: {}
    position:
      x: 300
      y: 100
```

## 开源协议

本项目基于 [ChatGPT-Mirai-QQ-Bot](https://github.com/lss233/chatgpt-mirai-qq-bot) 开发，遵循其 [开源协议](https://github.com/lss233/chatgpt-mirai-qq-bot/blob/master/LICENSE)

## 感谢

感谢 [ChatGPT-Mirai-QQ-Bot](https://github.com/lss233/chatgpt-mirai-qq-bot) 的作者 [lss233](https://github.com/lss233) 提供框架支持
