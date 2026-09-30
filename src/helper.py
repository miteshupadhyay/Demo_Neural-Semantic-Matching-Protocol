import fitz
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY =os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def extract_text_from_pdf(uploaded_file):
    """ 
    Extract text from PDF files.

    Args:
        pdf_path(str): The Path of the PDF File

    Returns:
        str: The Extracted text.
    """

    doc = fitz.open(stream=uploaded_file.read(),filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def ask_openai(prompt, max_tokens= 500):
    """ 
    Sends a prompt to the OpenAI API and returns the response.

    Args:
        prompt (str): The Prompt to send to the OpenAI API
        model (str): The LLM Model to use for the request
        temperature (float): The temperature for the response.

    Returns:
        str: The Response from the OpenAI API.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role":"user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content



  