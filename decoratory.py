def dekorator(func):
    def otoczka():
        print("-------------")
        func()
        print("=============")
    return otoczka

@dekorator
def hello():
    print ('No niemaneczko :)')

hello()

"""
lepszy przykład użycia dekoratora:"""

def db_connect(func):
    def wrapper():
        # połaczenie z bazą
        func()
        # zamknięcie połaczenia
    return wrapper

@db_connect
def dodanie_usera_do_bazy():
    pass
    # akcje dodawania usera, ale bez połączenia do bazy i zamknięcie połaczenia



