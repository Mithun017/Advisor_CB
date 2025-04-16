from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def store_memory(user_id, text, response, embedding, metadata):
    supabase.table("memory").insert({
        "user_id": user_id,
        "text": text,
        "response": response,
        "embedding": embedding,
        "metadata": metadata
    }).execute()

def retrieve_memories(user_id):
    return supabase.table("memory").select("*").eq("user_id", user_id).execute()
