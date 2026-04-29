from dyntaint import *

# Mark unstrusted sources
raw_input = untrusted(raw_input)

@untrusted
def obtain_number(mensaje="Ingrese un numero: "):
    n = raw_input(mensaje)
    return n

@cleaner(SQLI)
def exampleSQLi(s):
    '''lo limpie, creeme.'''
    return s

@ssink()
def guardarDB(valor):
    print "Guardando en la BD:", valor

if __name__ == '__main__':
    n = obtain_number()
    guardarDB(n) #throws runtime error as source (untrusted) reaches sink
    
