# DACAE Workspace Knowledge Graph

# DACAE Codebase Knowledge Graph

This graph maps the files, structure, and dependencies for token-efficient RAG.

## 📂 Indexed Files & Modules
- **[auto_sync.py](./auto_sync.py)** -> Linked to DACAE Core
- **[auto_watchdog.py](./auto_watchdog.py)** -> Linked to DACAE Core
- **[db_connector.py](./db_connector.py)** -> Linked to DACAE Core
- **[graph_rag.py](./graph_rag.py)** -> Linked to DACAE Core
- **[memory_core.py](./memory_core.py)** -> Linked to DACAE Core

## 🔗 Relationship Map
- `memory_core.py` ➔ Connects to `db_connector.py` (Supabase Cloud)
- `graph_rag.py` ➔ Feeds token-optimized markdown maps into Supabase

