import os
import openai
import os

strings = ['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',
           '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',
           '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',
           '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',
           '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'
           ]
for i, string in enumerate(strings):
    env_variable_name = f'ENV_VARIABLE_NAME{i}'
    os.environ[env_variable_name] = string
    openai.api_key = os.getenv(env_variable_name)
    print(openai.api_key)

def get_completion(prompt, model="gpt-3.5-turbo"): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# Summarize with a word/sentence/character limit

text = [
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for speling abilitty"  # spelling
]
for t in text:
    prompt = f"""Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    and errors, just say "No errors found". Don't use 
    any punctuation around the text:
    ```{t}```"""
    response = get_completion(prompt)
    print(response)