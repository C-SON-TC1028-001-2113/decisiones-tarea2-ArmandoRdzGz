def main():
    #escribe tu código abajo de esta línea
    
    edad = int(input('Ingresa tu edad: '))
    mayorEd = edad >= 18
    menorEd = edad > 0

    if mayorEd and menorEd:
        idenOf = str(input('¿Tienes identificación oficial? (s/n): '))
        if idenOf == 's' :
            print ('Trámite de licencia concedido')
        elif idenOf == 'n':
            print('No cumples requisitos')
        else:
            print('Respuesta incorrecta')
    if not mayorEd and menorEd :
        print('No cumples requisitos')
    if not mayorEd and not menorEd :
        print('Respuesta incorrecta')

if __name__=='__main__':
    main()

