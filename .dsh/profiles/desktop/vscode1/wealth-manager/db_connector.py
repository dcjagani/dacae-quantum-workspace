import os
from supabase import create_client, Client

# DACAE Official Fresh Supabase Credentials
SUPABASE_URL = "તમારું_નવું_URL_અહીં_મૂકવું"
SUPABASE_KEY = "lzzpackilabwbyoujuxp"

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