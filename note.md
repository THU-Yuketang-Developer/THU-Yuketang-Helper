# ZhiPu AI 调用示例

[API 文档](https://open.bigmodel.cn/dev/api/)

## 请求示例

```python
from zhipuai import ZhipuAI
client = ZhipuAI(api_key="")  # 请填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4",  # 请填写您要调用的模型名称
    messages=[
        {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"},
        {"role": "assistant", "content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"},
        {"role": "user", "content": "智谱AI开放平台"},
        {"role": "assistant", "content": "点燃未来，智谱AI绘制无限，让创新触手可及！"},
        {"role": "user", "content": "创作一个更精准且吸引人的口号"}
    ],
)
print(response.choices[0].message)
```

## 响应示例

```
{
  "created": 1703487403,
  "id": "8239375684858666781",
  "model": "glm-4",
  "request_id": "8239375684858666781",
  "choices": [
      {
          "finish_reason": "stop",
          "index": 0,
          "message": {
              "content": "以AI绘蓝图 — 智谱AI，让创新的每一刻成为可能。",
              "role": "assistant"
          }
      }
  ],
  "usage": {
      "completion_tokens": 217,
      "prompt_tokens": 31,
      "total_tokens": 248
  }
}
```

---

以下是 response 的例子：

```
Completion(model='glm-4', created=1729689992, choices=[CompletionChoice(index=0, finish_reason='stop', message=CompletionMessage(content='你好！有什么我可以帮助你的吗？', role='assistant', tool_calls=None))], request_id='202410232126324ca1ddecc9bc4596', id='202410232126324ca1ddecc9bc4596', usage=CompletionUsage(prompt_tokens=7, completion_tokens=10, total_tokens=17))
```

```
Completion(model='glm-4', created=1729690109, choices=[CompletionChoice(index=0, finish_reason='stop', message=CompletionMessage(content='你好👋！我是人工智能助手智谱清言，可以叫我小智🤖，很高兴见到你，欢迎问我任何问题。', role='assistant', tool_calls=None))], request_id='2024102321282863f6852dbb964d29', id='2024102321282863f6852dbb964d29', usage=CompletionUsage(prompt_tokens=7, completion_tokens=32, total_tokens=39))
```

以下是 response.choices[0].message 的例子：

```
CompletionMessage(content='你好👋！我是人工智能助手智谱清言，可以叫我小智🤖，很高兴见到你， 欢迎问我任何问题。', role='assistant', tool_calls=None)
```

以下是 response.choices[0].message.content 的例子：

```
当然可以，请告诉我您遇到的问题，我会尽力提供帮助。
```