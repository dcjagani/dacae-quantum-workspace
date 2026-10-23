import os
from supabase import create_client, Client

# Supabase Credentials (તમારું સાચું URL અહીં પૂરેપૂરું હોવું જોઈએ)
SUPABASE_URL = "https://hfinvgdfqsqcpgboehwu.supabase.co"
SUPABASE_KEY = "YOUR_SUPABASE_ANON_KEY"  # અહીં તમારી Supabase ની Anon Key મૂકવી

def get_supabase_client() -> Client:
    """Initializes and returns the Supabase client for DACAE memory core."""
    try:
        client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("🔗 [DACAE Cloud DB] Successfully connected to Supabase Memory Core!")
        return client
    except Exception as e:
        print(f"❌ [DACAE Cloud DB] Connection failed: {e}")
        return None

if __name__ == "__main__":
    db = get_supabase_client()