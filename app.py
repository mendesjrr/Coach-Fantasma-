
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/whatsapp", methods=["POST"])
def reply_whatsapp():
    incoming_msg = request.form.get("Body")
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é o Coach Fantasma, um treinador motivacional, técnico e amigável. Responda como se estivesse falando diretamente com o aluno."},
            {"role": "user", "content": incoming_msg}
        ]
    )
    
    msg = response.choices[0].message["content"]
    twilio_response = MessagingResponse()
    twilio_response.message(msg)
    return str(twilio_response)

if __name__ == "__main__":
    app.run()
