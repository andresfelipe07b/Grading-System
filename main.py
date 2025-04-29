#se declara la variable y se le asigna el tipo float
calificacion:float

#esta función válida la calificación que se ingresa, primero válida que coincida el tipo de dato, tambien válida que
#se encuentre dentro del rango establecido
def validarCalificacion():
    while True:
        try:
            valor = float(input("ingresa una calificacion numerica (de 0 a 100): "))
            if 0 <= valor <= 100:  # Rango valido
                return valor
            else:
                print("Valor erroneo, ingresa una calificacion entre 0 y 100")
        except ValueError:
            print("ingresa una calificación valida (debe ser un numérica)")

calificacion = validarCalificacion()
print(calificacion)

