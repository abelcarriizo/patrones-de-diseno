from abc import ABC, abstractmethod

class NotificationSender(ABC):
  @abstractmethod
  def send(self, message):
    pass

class EmailSender(NotificationSender):
  def send(self, message):
    print(f'Enviando correo: {message}')

class SMSSender(NotificationSender):
  def send(self, message):
    print(f'Enviando SMS: {message}')

class NotificationService:
  def __init__(self, sender: NotificationSender):
    self.sender = sender

  def notify(self, message):
    self.sender.send(message)

if __name__=='__main__':
  email = EmailSender()
  notification_service = NotificationService(email)
  notification_service.notify('Hola, este es un mensaje de prueba!')