import openai

openai.api_key ="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"

def ask(q):
	response = openai.Completion.create(engine="davinci",prompt=f"Q:{q}\nA:",max_tokens=1024,n=1,stop=None,temperature=0.7,)
	return response.choices[0].text.strip()

q=input("enter question")
response = ask(q)
print(response)
