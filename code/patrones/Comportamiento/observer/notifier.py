from observer import Observer

class NewsPublisher:  # El "canal de noticias"
    def __init__(self):
        self.subscribers = []  # Lista de observadores

    def subscribe(self, observer: Observer):
        self.subscribers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.subscribers.remove(observer)

    def notifySubscribers(self, message: str):
        for subscriber in self.subscribers:
            subscriber.update(message)
