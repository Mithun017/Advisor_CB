from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai
from supabase import create_client
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
# Simpler CORS configuration
CORS(app)

# Supabase setup
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Gemini setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.0-flash")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_id = data.get("user_id")
        query = data.get("query")
        
        if not query:
            return jsonify({"error": "Query is required"}), 400
            
        response = model.generate_content(query).text

        # Store chat in Supabase
        try:
            supabase.table("memory").insert({
                "user_id": user_id,
                "text": query,
                "response": response,
                "embedding": [0.0] * 768,  # Placeholder
                "metadata": {}
            }).execute()
        except Exception as e:
            print("Supabase error:", str(e))
            # Continue even if storage fails
            
        return jsonify({"response": response})
        
    except Exception as e:
        print("Error in chat endpoint:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route("/history", methods=["GET"])
def history():
    user_id = request.args.get("user_id")
    result = supabase.table("memory")\
        .select("text, response")\
        .eq("user_id", user_id)\
        .order("id", desc=False)\
        .execute()

    chats = [{"query": item["text"], "response": item["response"]} for item in result.data]
    return jsonify({"history": chats})

@app.route("/history", methods=["DELETE"])
def clear_history():
    user_id = request.args.get("user_id")
    result = supabase.table("memory").delete().eq("user_id", user_id).execute()
    return jsonify({"status": "cleared", "details": result.data})

if __name__ == "__main__":
    app.run(debug=True)
