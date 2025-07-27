#save char hostroy in firestore DB 

from langchain_groq import ChatGroq
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
llm = ChatGroq(model="gemma2-9b-it", temperature=0
             )



PROJECT_ID = "langchain-chatbot-3de42"
COLLECTION_NAME = "msgs_history"
SESSION_ID = "user_name"

print("initialising Firestore Client....")
client = firestore.Client(project=PROJECT_ID)

print("Initialising Firestore Chat Message History...")
chat_history= FirestoreChatMessageHistory(session_id = SESSION_ID, collection=COLLECTION_NAME, 
    client=client)


    
print("Chat History Initialised")
print("Current chat hostory: ", chat_history.messages)

print("Start chatting with the AI, press XX to exit")
while True:
    system_message= SystemMessage(content="You are an helpful AI assitant")
    user_input = input("User: ")
    if(user_input=="XX" or user_input=="xx"):
        break


    chat_history.add_messages([system_message, HumanMessage(content=user_input)])


    response = llm.invoke(chat_history.messages)
    chat_history.add_messages([AIMessage(content=response.content)])
    print("AI: " + response.content)
