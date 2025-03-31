import requests
import json

class TeamsNotifier:
    def __init__(self, webhook_url: str):
        """Inicializa el notificador con la URL del webhook de Teams."""
        self.webhook_url = webhook_url

    def send_alert(self, message: str, title: str = "Alerta"):
        """Envía una alerta a Microsoft Teams."""
        payload = {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "summary": title,
            "themeColor": "0076D7",
            "title": title,
            "text": message
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post(self.webhook_url, headers=headers, data=json.dumps(payload))

        if response.status_code != 200:
            raise Exception(f"Error enviando alerta: {response.status_code} - {response.text}")
