import os
from memory_core import DACAEMemoryCore

class DACAEGraphRAG:
    """Scans the workspace, builds a lightweight Knowledge Graph in Markdown, 
    and saves it to Supabase cloud memory to save tokens."""
    
    def __init__(self, target_folder="wealth-manager"):
        self.target_folder = target_folder
        self.memory_core = DACAEMemoryCore()
        
    def build_codebase_graph(self):
        """Scans python and markdown files and creates a linked markdown map."""
        print(f"🔍 [GraphRAG] Scanning directory: {self.target_folder}...")
        
        graph_content = "# DACAE Codebase Knowledge Graph\n\n"
        graph_content += "This graph maps the files, structure, and dependencies for token-efficient RAG.\n\n"
        
        file_list = []
        
        for root, dirs, files in os.walk(self.target_folder):
            # Skip export and virtual environment folders
            if "exports" in dirs:
                dirs.remove("exports")
            if ".venv" in dirs:
                dirs.remove(".venv")
                
            for file in files:
                if file.endswith((".py", ".md", ".json", ".sql")):
                    rel_path = os.path.relpath(os.path.join(root, file), self.target_folder)
                    file_list.append(rel_path)
                    
        # Build linked markdown structure
        graph_content += "## 📂 Indexed Files & Modules\n"
        for f in file_list:
            graph_content += f"- **[{f}](./{f})** -> Linked to DACAE Core\n"
            
        graph_content += "\n## 🔗 Relationship Map\n"
        graph_content += "- `memory_core.py` ➔ Connects to `db_connector.py` (Supabase Cloud)\n"
        graph_content += "- `graph_rag.py` ➔ Feeds token-optimized markdown maps into Supabase\n"
        
        title = "DACAE Workspace Knowledge Graph"
        
        # 1. Save to Supabase Cloud Memory
        self.memory_core.save_to_supabase(
            category="GraphRAG",
            title=title,
            content=graph_content
        )
        
        # 2. Save As Local Markdown Backup
        saved_file = self.memory_core.save_as_local_file(
            title=title,
            content=graph_content,
            file_format="md",
            folder="exports"
        )
        
        print(f"✅ [GraphRAG] Knowledge Graph successfully generated and saved!")
        return saved_file

if __name__ == "__main__":
    rag = DACAEGraphRAG()
    rag.build_codebase_graph()