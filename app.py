import requests
from flask import Flask, jsonify
import os
import openai

openai.api_key = os.getenv('OPENAI_KEY')

app = Flask(__name__) 

@app.route("/service/<string:question>")

def synopsis(book):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"give a summary of book in 1000 words\n\nbook:{book}:\n\n.",
      temperature=0.65,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    generated_text=response.choices[0].text.strip()
    return generated_text

def chat(system, user_assistant):
  assert isinstance(system, str), "`system` should be a string"
  assert isinstance(user_assistant, list), "`user_assistant` should be a list"
  system_msg = [{"role": "system", "content": system},
                # {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                {"role": "user", "content": "Where was it played?"}
                ]
  user_assistant_msgs = [
      {"role": "assistant", "content": user_assistant[i]} if i % 2 else {"role": "user", "content": user_assistant[i]}
      for i in range(len(user_assistant))]

  msgs = system_msg+ user_assistant_msgs
  response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=msgs)
  status_code = response["choices"][0]["finish_reason"]
  assert status_code == "stop", f"The status code was {status_code}."
  return response["choices"][0]["message"]["content"]
system=input("How do I behave like mentor or friend")
user_input=input("enter your interest")
response_fn_test = chat(f"You are a {system}.",[f"I am interested in {user_input} suggest me the education path for the same in structured format"])

print((response_fn_test))