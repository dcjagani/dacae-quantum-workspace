import os
import json
from db_connector import get_supabase_client

class DACAEMemoryCore:
    """Manages persistent cloud memory (Supabase) and local file storage (Save As) for DACAE."""
    
    def __init__(self):
        self.client = get_supabase_client()
        
    def save_to_supabase(self, category: str, title: str, content: str):
        """1. Save data to Supabase Cloud Database."""
        if not self.client:
            print("❌ [DACAE Cloud] Supabase client not initialized.")
            return False
            
        try:
            data = {
                "category": category,
                "title": title,
                "content": content
            }
            response = self.client.table("dacae_memory").insert(data).execute()
            print(f"✅ [DACAE Cloud] Successfully saved '{title}' to Supabase Core!")
            return response
        except Exception as e:
            print(f"❌ [DACAE Cloud] Error saving to Supabase: {e}")
            return None

    def save_as_local_file(self, title: str, content: str, file_format: str = "md", folder: str = "exports"):
        """2. 'Save As' functionality to export memory as Markdown (.md) or JSON (.json) locally."""
        try:
            os.makedirs(folder, exist_ok=True)
            # Safe filename generation
            safe_title = "".join(c if c.isalnum() else "_" for c in title).lower()
            
            if file_format.lower() == "json":
                filename = os.path.join(folder, f"{safe_title}.json")
                file_data = {"title": title, "content": content}
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(file_data, f, indent=4, ensure_ascii=False)
            else:
                # Default Markdown (.md) save format
                filename = os.path.join(folder, f"{safe_title}.md")
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"# {title}\n\n{content}\n")
                    
            print(f"💾 [DACAE Save As] Successfully saved local backup to: {filename}")
            return filename
        except Exception as e:
            print(f"❌ [DACAE Save As] Error saving local file: {e}")
            return None

if __name__ == "__main__":
    # Test both Supabase Save and Save As local file
    memory = DACAEMemoryCore()
    
    title_text = "Air LLM & Cloud Integration"
    content_text = "Integrated layer-by-layer execution concepts and cloud memory persistence for zero-cost operation."
    
    # 1. Save in Supabase Cloud
    memory.save_to_supabase(category="Architecture", title=title_text, content=content_text)
    
    # 2. Save As Local File (.md or .json)
    memory.save_as_local_file(title=title_text, content=content_text, file_format="md")