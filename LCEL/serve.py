import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from langserve import add_routes


load_dotenv()

grop_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(model='gemma2-9b-it', api_key=grop_api_key)

# Prompt Generation 
generic_prompt = "translate the following text into {language}"
prompt = ChatPromptTemplate.from_messages (
    [("system" , generic_prompt),("user","{text}")]
)

parser = StrOutputParser()

##create chain
chain = prompt|model|parser

# App Defination
app = FastAPI(
    title="Langchain Server",
            version="1.0",
            description="A simple API server using Langchain runnable interfaces"
            )


add_routes(
    app,
    chain,
    path = "/chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)






