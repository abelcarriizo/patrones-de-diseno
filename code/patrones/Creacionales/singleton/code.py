class Singleton:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance == None:
      cls._instance = super(Singleton, cls).__new__(cls)
    return cls._instance