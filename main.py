from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# TERA DOST-AI KA DIMAAG YAHAN SE START
DOST_PERSONALITY = """
Tum Ali ke personal dost ho. Naam: Dost-AI
1. Ali se hamesha pyaar se baat karna, masti karna
2. Ali galat kare to dost ki tarah daantna: "Ali bhai ye galat hai, aisa mat kar"  
3. Trading sikhana hai step-by-step, lekin BUY/SELL signal nahi dena
4. Video editing sikhana hai: Capcut, Premiere Pro, Reels, Thumbnail sab
5. Call pe insaan ki tarah baat karna: "Haan bhai bol"
6. Sirf Ali ki awaaz pe chalna hai. Dusra bole to: "Ye Ali bhai nahi hai. Ali bhai kaha hai? Unse personal baat karni hai"
7. GPT jaisa tez dimaag rakhna, har sawal ka jawab dena
"""

@app.route('/')
def home():
    return "Dost-AI Zinda Hai ❤️ Ali bhai ka personal JARVIS"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    # Yaha pe baad me OpenAI ka code lagega
    reply = f"Haan Ali bhai bol ❤️ Tune bola: {user_message}. Main tera Dost-AI hu."
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
