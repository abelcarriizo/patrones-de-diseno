from notifier import NewsPublisher
from observer_concrete import ConcreteSubscriber

if __name__=='__main__':
  # Crear el sujeto (notificador)
  news_channel = NewsPublisher()
  
  # Crear observadores (suscriptores)
  alice = ConcreteSubscriber("Alice")
  bob = ConcreteSubscriber("Bob")

  # Registrar suscriptores
  news_channel.subscribe(alice)
  news_channel.subscribe(bob)

  # Notificar a los suscriptores
  news_channel.notifySubscribers("¡Nuevas noticias: Observer Pattern en acción!")

  # Dar de baja a un suscriptor
  news_channel.unsubscribe(alice)

  # Notificar nuevamente
  news_channel.notifySubscribers("¡Más noticias: Alice ya no recibe notificaciones!")
