import os
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


openai_api_key = os.environ["OPENAI_API_KEY"]
chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=openai_api_key
)

template = """ 
You are an agent that's not talkative and only returns data in JSON format.
You take as input a customer feedback that could be as little as one words.
With the feedback the agent then outputs data with the following schema: sentiment: string, topics: [string], message: string.
1. You must analyze the customer feedback to determine the overall sentiment.
2. You must extract topics, only if those topics caused said sentiment (topics in spanish).
3. You must generate a message to make the client feel like he's understood.
Available output values for overall sentiment: ["positivo", "neutral", "negativo"].

Client Feedback: {feedback}

JSON Response only: 
"""

prompt=PromptTemplate(
    template=template,
    input_variables=["feedback"],
)
system_message_prompt = SystemMessagePromptTemplate(prompt=prompt)

human_template="{feedback}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

chain = LLMChain(llm=chat, prompt=chat_prompt)
