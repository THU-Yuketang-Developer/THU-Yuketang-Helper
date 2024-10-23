# Problem Format 记录

记录接受到的 message 中 problem 的 json 格式：

以下是一些示例

```json
{
    "problemId": "1269254406812402176",
    "problemType": 1, // 1 为单选题
    "body": "此处添加题目描述", // 题目描述
    "score": 100, // 分数
    "remark": "",
    "answers": [],
    "sendTime": 0,
    "limit": 0,
    "options": [ // 选项
        {"key": "A", "value": "1"},
        {"key": "B", "value": "13"},
        {"key": "C", "value": "2"},
        {"key": "D", "value": "4"}
    ],
    //元素布局信息，不重要
    "submit": {"width": 121.5,"height": 32.4,"top": 489.35,"left": 702.0},
    "bullets": [{"width": 40.5,"height": 40.5,"top": 224.4,"label": "A","left": 123.75},{"width": 40.5,"height": 40.5,"top": 291.9,"label": "B","left": 123.75},{"width": 40.5,"height": 40.5,"top": 359.4,"label": "C","left": 123.75},{"width": 40.5,"height": 40.5,"top": 426.9,"label": "D","left": 123.75}],
    "hasRemark": false,
    "version": 4,
    "result": null
}
```

```json
{
    "problemId": "1269254406829179392",
    "problemType": 2, // 2 为多选题
    "body": "此处添加题目描述",
    "score": 100,
    "remark": "",
    "answers": [],
    "sendTime": 0,
    "limit": 0,
    "options": [ // 选项
        {"key": "A", "value": "1"},
        {"key": "B", "value": "3"},
        {"key": "C", "value": "2"},
        {"key": "D", "value": "9"}
    ],
    "halfScore": 0,
    "submit": {}, // 略
    "bullets":[], // 略
    "hasRemark": false,
    "version": 4,
    "result": null
}
```

```json
{
    "problemId": "1269254406837568000",
    "problemType": 3, // 3 为投票题
    "body": "此处添加投票内容",
    "score": 0,
    "remark": "",
    "answers": [],
    "sendTime": 0,
    "limit": 0,
    "options": [ // 选项
        {"key": "A", "value": "2"},
        {"key": "B", "value": "3"},
        {"key": "C", "value": "4"},
        {"key": "D", "value": "5"}
    ],
    "anonymous": false, // 是否匿名
    "pollingCount": 1,
    "submit": {}, // 略
    "bullets":[], // 略
    "hasRemark": false,
    "version": 4,
    "result": null
}
```

```json
{
    "problemId": "1269254406854345216",
    "problemType": 4, // 4 为填空题
    "body": "1111 [填空1] 3333 [填空2] 5566 [填空3] 889。", // 题目描述
    "score": 300,
    "remark": "",
    "answers": [],
    "sendTime": 0,
    "limit": 0,
    "blanks": [ // 每个空的相关信息
        {
            "num": 1,
            "score": 100,
            "answers": [],
            "fuzzyMatch": true,
            "caseSensitive": false
        },{
            "num": 2,
            "score": 100,
            "answers": [],
            "fuzzyMatch": false,
            "caseSensitive": true
        },{
            "num": 3,
            "score": 100,
            "answers": [],
            "fuzzyMatch": true,
            "caseSensitive": true
        }
    ],
    "orderInsensitive": false, // 是否顺序无关
    "pollingCount": 0,
    "submit": {}, // 略
    "hasRemark": false,
    "version": 4,
    "result": null
}
```

```json
{
    "problemId": "1269254406879511040",
    "problemType": 5, // 5 为简答题
    "body": "啊啊啊啊啊啊啊啊",
    "score": 1000,
    "remark": "",
    "answers": [],
    "sendTime": 0,
    "limit": 0,
    "submit": {
        "width": 121.5,
        "height": 32.4,
        "top": 489.375031,
        "left": 702.0
    },
    "hasRemark": false,
    "version": 4,
    "result": null
}