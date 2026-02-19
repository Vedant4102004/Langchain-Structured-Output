from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from typing import TypedDict

load_dotenv()

# Use a model that supports Tool Calling / Structured Output
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct", 
    task="text-generation" 
)

model = ChatHuggingFace(llm=llm)

class Review(TypedDict):
    summary: str
    sentiment: str

# This wraps the model to force JSON output based on your TypedDict
structured_model = model.with_structured_output(Review)

text = """I recently upgraded to the Samsung Galaxy S24 Ultra... (your text)"""

result = structured_model.invoke(text)

# FIX: Access keys that actually exist in your TypedDict
print(f"Summary: {result['summary']}")
print(f"Sentiment: {result['sentiment']}")