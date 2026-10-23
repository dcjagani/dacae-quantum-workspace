import os
import subprocess

def git_auto_sync():
    print("🚀 DACAE Quantum Workspace: Auto-Sync Initiated...")
    
    try:
        # Check git status
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not status.stdout.strip():
            print("✨ Workspace is already clean and up-to-date with GitHub!")
            return

        # Add all changes
        print("📦 Staging changes securely...")
        subprocess.run(["git", "add", "."], check=True)

        # Commit with timestamp
        commit_msg = "Auto-sync: DACAE workspace update towards ultimate result"
        print(f"📝 Committing changes: '{commit_msg}'")
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)

        # Push to GitHub main branch
        print("☁️ Pushing to GitHub repository (dacae-quantum-workspace)...")
        subprocess.run(["git", "push", "origin", "main"], check=True)

        print("🎉 Success! DACAE workspace successfully synced with Cloud.")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git Sync Error: Please check your repository status or authentication. Details: {e}")

if __name__ == "__main__":
    git_auto_sync()