import os
import requests

class UltimateFailsafeRouter:
    """
    DACAE Project Master Failsafe Router (FreeLLMAPI Inspired & Google-Free)
    Hierarchy Order:
    1. OmniRoute (Local/Self-hosted Gateway)
    2. OpenRouter Free Endpoint ('openrouter/free')
    3. Groq API (Ultra-fast Llama 3)
    4. Hugging Face Serverless API
    5. Cloudflare Workers AI
    """
    def __init__(self):
        self.omniroute_url = os.environ.get("OMNIROUTE_BASE_URL", "http://localhost:20128/v1")
        self.omniroute_key = os.environ.get("OMNIROUTE_API_KEY", "dummy")
        
        self.openrouter_key = os.environ.get("OPENROUTER_API_KEY")
        self.groq_key = os.environ.get("GROQ_API_KEY")
        self.hf_key = os.environ.get("HUGGINGFACE_API_KEY")
        self.cf_account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
        self.cf_token = os.environ.get("CLOUDFLARE_API_TOKEN")

    def generate(self, prompt: str) -> str:
        
        # ૧. પ્રથમ પ્રયાસ: OmniRoute Gateway
        try:
            response = self._call_omniroute(prompt)
            if response:
                return f"[FreeLLM Router: OmniRoute] {response}"
        except Exception as e:
            print(f"OmniRoute skipped/failed: {e}")

        # ૨. બીજો પ્રયાસ: OpenRouter Free Endpoint
        if self.openrouter_key:
            try:
                response = self._call_openrouter(prompt)
                if response:
                    return f"[FreeLLM Router: OpenRouter-Free] {response}"
            except Exception as e:
                print(f"OpenRouter free failed: {e}")

        # ૩. ત્રીજો પ્રયાસ: Groq API Backup
        if self.groq_key:
            try:
                response = self._call_groq(prompt)
                if response:
                    return f"[FreeLLM Router: Groq Backup] {response}"
            except Exception as e:
                print(f"Groq backup failed: {e}")

        # ૪. ચોથો પ્રયાસ: Hugging Face Serverless API
        if self.hf_key:
            try:
                response = self._call_huggingface(prompt)
                if response:
                    return f"[FreeLLM Router: HuggingFace] {response}"
            except Exception as e:
                print(f"HuggingFace failed: {e}")

        # ૫. પાંચમો પ્રયાસ: Cloudflare Workers AI
        if self.cf_account_id and self.cf_token:
            try:
                response = self._call_cloudflare(prompt)
                if response:
                    return f"[FreeLLM Router: Cloudflare] {response}"
            except Exception as e:
                print(f"Cloudflare failed: {e}")

        return "Critical Error: All free open-source gateway nodes and failsafes exhausted."

    def _call_omniroute(self, prompt):
        url = f"{self.omniroute_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.omniroute_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "auto",
            "messages": [{"role": "user", "content": prompt}]
        }
        res = requests.post(url, headers=headers, json=data, timeout=8)
        if res.status_code == 200:
            return res.json()['choices'][0]['message']['content']
        raise Exception(f"OmniRoute Status: {res.status_code}")

    def _call_openrouter(self, prompt):
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.openrouter_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "openrouter/free",
            "messages": [{"role": "user", "content": prompt}]
        }
        res = requests.post(url, headers=headers, json=data, timeout=10)
        if res.status_code == 200:
            return res.json()['choices'][0]['message']['content']
        raise Exception(f"OpenRouter Status: {res.status_code}")

    def _call_groq(self, prompt):
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.groq_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}]
        }
        res = requests.post(url, headers=headers, json=data, timeout=8)
        if res.status_code == 200:
            return res.json()['choices'][0]['message']['content']
        raise Exception(f"Groq Status: {res.status_code}")

    def _call_huggingface(self, prompt):
        url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
        headers = {
            "Authorization": f"Bearer {self.hf_key}",
            "Content-Type": "application/json"
        }
        data = {"inputs": prompt}
        res = requests.post(url, headers=headers, json=data, timeout=10)
        if res.status_code == 200:
            result = res.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get("generated_text", "")
        raise Exception(f"HuggingFace Status: {res.status_code}")

    def _call_cloudflare(self, prompt):
        url = f"https://api.cloudflare.com/client/v4/accounts/{self.cf_account_id}/ai/run/@cf/meta/llama-3-8b-instruct"
        headers = {
            "Authorization": f"Bearer {self.cf_token}",
            "Content-Type": "application/json"
        }
        data = {"prompt": prompt}
        res = requests.post(url, headers=headers, json=data, timeout=10)
        if res.status_code == 200:
            return res.json().get('result', {}).get('response', '')
        raise Exception(f"Cloudflare Status: {res.status_code}")

if __name__ == "__main__":
    router = UltimateFailsafeRouter()
    print(router.generate("DACAE system test with FreeLLMAPI multi-provider setup."))