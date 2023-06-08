import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)