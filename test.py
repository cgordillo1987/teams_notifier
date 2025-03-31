from teams_notifier.notifier import TeamsNotifier

# Reemplaza con la URL de tu webhook de Teams
webhook_url = "https://greensqa.webhook.office.com/webhookb2/710cee65-923e-4606-989d-824609735810@708209e8-a060-41b2-8bbe-cb5825e3f398/IncomingWebhook/9f2f42bfc8ad4e75a305b46e940f2eca/a1edd493-dee6-4437-8010-a88f95bad0bf/V2oykBz1iRxJQU_RpQCz4BwD44MBRrbiSIsFugyVfQdPA1"
notifier = TeamsNotifier(webhook_url)

notifier.send_alert("Prueba de alerta desde Python con Poetry", "Test de Notificación")
