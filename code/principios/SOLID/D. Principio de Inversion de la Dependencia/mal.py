class EmailService:
  def send_email(self, message):
    print(f'Enviando correo: {message}')

class NotificationService:
  def __init__(self):
    self.email_service = EmailService()

  def notify(self, message):
    self.email_service.send_email(message)

notifier = NotificationService()
notifier.notify('Hola, esto es una prueba!')