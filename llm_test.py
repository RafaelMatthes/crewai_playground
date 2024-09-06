
# azure_llm = ChatOpenAI(
#         base_url='https://cognaai-west-us.openai.azure.com',
#         api_key='a2e32b70b6964cb9bc8f37204e397854',
#         model="gpt-4o"
# )

from langchain_openai import AzureChatOpenAI


azure_llm = AzureChatOpenAI(
    api_key='a2e32b70b6964cb9bc8f37204e397854',
    azure_endpoint='https://cognaai-west-us.openai.azure.com',
    api_version='2024-02-15-preview',
    azure_deployment='gpt-4o'
)

try:
    result = azure_llm.invoke("olá! como você está?")
    print(result)

except Exception as e:
    print(e)
