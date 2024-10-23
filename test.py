from Scripts.Utils import get_zhipuai_response

question = "你可以帮我解决一个问题吗？"

answer = get_zhipuai_response(question)

print("--------------------")

print(answer)

print("Done!")