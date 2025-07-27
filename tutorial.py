from langchain_groq import ChatGroq
from langchain_core.messages    import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv


load_dotenv()

llm = ChatGroq(model="gemma2-9b-it", temperature=0)
chat_history =[]

system_message = SystemMessage(content="You are a helpful AI assistant")
chat_history.append(system_message)

print("Press XX to exit the chat")

while True:
    user_input = input("You:")
    if user_input == "XX":
        break
    chat_history.append(HumanMessage(content=user_input))
    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI: "+ response.content)
