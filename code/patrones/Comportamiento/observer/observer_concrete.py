from observer import Observer

class ConcreteSubscriber(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f'{self.name} recibió la noticia: {message}')
