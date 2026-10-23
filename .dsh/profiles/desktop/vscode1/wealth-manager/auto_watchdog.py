import time
import subprocess
import os

def run_sync():
    print("🔄 [DACAE Watchdog] Changes detected! Auto-syncing with GitHub...")
    try:
        subprocess.run(["python", "wealth-manager/auto_sync.py"], check=True)
        print("✨ [DACAE Watchdog] Successfully synced to cloud!")
    except Exception as e:
        print(f"❌ [DACAE Watchdog] Sync failed: {e}")

if __name__ == "__main__":
    print("🚀 DACAE Background Auto-Watchdog is active and running...")
    print("💡 It will monitor your workspace and keep GitHub updated automatically.")
    
    # Simple polling loop to check git status every 60 seconds
    while True:
        try:
            status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
            if status.stdout.strip():
                run_sync()
        except Exception as e:
            print(f"⚠️ Error checking status: {e}")
        
        # Check every 60 seconds
        time.sleep(60)

