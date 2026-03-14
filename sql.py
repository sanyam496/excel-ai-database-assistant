# from langchain_community.utilities import SQLDatabase
# from langchain_community.agent_toolkits import create_sql_agent

# from langchain_google_genai import ChatGoogleGenerativeAI


# db=SQLDatabase.from_uri("sqlite:///company.db")
# llm = ChatGoogleGenerativeAI(
#     model="gemini-3.1-flash-lite-preview",
#     google_api_key="AIzaSyCag3FVXY11kmuUElj_y9zLATr5DZOdWm4"
# )
# agent= create_sql_agent(
#     llm=llm,
#     db=db,
#     agent_type="zero-shot-react-description",
#     verbose=True,
#     handle_parsing_errors=True,
#     top_k=10
# )
# # schema_description = """
# # Tables available:

# # PURCHASE_TABLE
# # - PUR_NO
# # - PUR_DATE
# # - VENDOR
# # - ITEM_NAME
# # - QTY
# # - UNIT_RATE
# # - ITEM_AMOUNT
# # - BILL_AMT
# # - SITE_NAME

# # PO_TABLE
# # - PO_NO
# # - PO_DATE
# # - ITEM_NAME
# # """
# # def ask_database(question):
# #     response = agent.invoke({"input": question})
# #     return response["output"]
# # def ask_database(question):
# #     try:
# #         response = agent.invoke({"input": question})
# #         return response["output"]
# #     except Exception as e:
# #         return f"Error processing query: {str(e)}"
# def ask_database(question):

#     try:

#         prompt = f"""
# You are an AI SQL assistant.

# You answer questions using a SQLite database.

# Tables available:

# 1. PURCHASE_TABLE
# 2. PO_TABLE

# Rules:
# - Always use SQL to retrieve data.
# - If the user asks for purchase data, use PURCHASE_TABLE.
# - If the user asks for PO data, use PO_TABLE.
# - Return clear answers.

# User Question:
# {question}
# """

#         response = agent.invoke({"input": prompt})

#         # safe return
#         if isinstance(response, dict) and "output" in response:
#             return response["output"]

#         return str(response)

#     except Exception as e:
#         return f"Database query failed: {str(e)}"
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_google_genai import ChatGoogleGenerativeAI


# -------------------------
# DATABASE CONNECTION
# -------------------------

db = SQLDatabase.from_uri("sqlite:///company.db")


# -------------------------
# LLM MODEL
# -------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite-preview",
    google_api_key="AIzaSyCag3FVXY11kmuUElj_y9zLATr5DZOdWm4",
    temperature=0,
    convert_system_message_to_human=True
)


# -------------------------
# SQL AGENT
# -------------------------

agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True,
    handle_parsing_errors=True,
    prefix="""
You are an AI SQL assistant.

Always return the final answer in this format:

Final Answer: <your answer>

Do not return plain text.
"""
)


# -------------------------
# ASK DATABASE FUNCTION
# -------------------------

def ask_database(question):

    print("\n==============================")
    print("STEP 1️⃣ USER QUESTION:")
    print(question)

    try:

        print("\nSTEP 2️⃣ SENDING QUESTION TO AGENT...\n")

        response = agent.invoke({"input": question})

        print("\nSTEP 3️⃣ AGENT RESPONSE RECEIVED")

        print("\nFULL RESPONSE OBJECT:")
        print(response)

        answer = response.get("output", str(response))

        print("\nSTEP 4️⃣ FINAL ANSWER:")
        print(answer)

        print("==============================\n")

        return answer

    except Exception as e:

        print("\n❌ ERROR OCCURRED DURING PROCESS")

        print("ERROR MESSAGE:")
        print(str(e))

        print("\nCHECK ABOVE STEPS TO IDENTIFY FAILURE POINT")

        return f"Database query failed: {str(e)}"