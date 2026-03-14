# from fastapi import FastAPI
# from sql import ask_database
# from fastapi.middleware.cors import CORSMiddleware

# app=FastAPI()

# # origins = [
# #     "http://127.0.0.1:5500",
# #     "http://localhost:5500",
# #     "http://127.0.0.1:8000",
# #     "http://localhost:8000",
# # ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/")
# def home():
#     return {"message":"Chatbot API running"}
# @app.get("/ask")
# def ask(question: str):
#     answer=ask_database(question)
#     return{"answer": answer}

# #========================
# # from fastapi import FastAPI
# # from sql import ask_database
# # from fastapi.middleware.cors import CORSMiddleware

# # app = FastAPI()

# # # Allow frontend origins
# # origins = [
# #     "http://127.0.0.1:5500",
# #     "http://localhost:5500",
# #     "http://127.0.0.1:8000",
# #     "http://localhost:8000",
# # ]

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=origins,
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # @app.get("/")
# # def home():
# #     return {"message": "Chatbot API running"}

# # @app.get("/ask")
# # def ask(question: str):
# #     answer = ask_database(question)
# #     return {"answer": answer}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sql import ask_database

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Excel AI Chatbot API running"}

@app.get("/ask")
def ask(question: str):
    answer = ask_database(question)
    return {"answer": answer}