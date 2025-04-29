#se declara la variable y se le asigna el tipo
initialGrade:float
grades: list[float]
grade: float
specificValue:float

#esta función válida la calificación que se ingresa, primero válida que coincida el tipo de dato, tambien válida que
#se encuentre dentro del rango establecido
def validateGrade():
    while True:
        try:
            value = float(input("ingresa una calificacion numerica (de 0 a 100): "))
            if 0 <= value <= 100:  # Rango valido
                return value
            else:
                print("Valor erroneo, ingresa una calificacion entre 0 y 100")
        except ValueError:
            print("ingresa una calificación valida (debe ser un numérica)")

#calcula el promedio de las calificaciones
def calculateAverage(gradeList: list[float]):
    sum = 0
    for grade in gradeList:
        sum += grade
    return sum / len(gradeList)

#solicita las calificaciones
def askGrades():
    grades = []
    for i in range(5):
        grade = input(f"Ingresa la calificacion {i+1}:")
        grades.append(float(grade))
    return grades

def countHigherGrades(gradeList: list[float], specificValue: float):
    counter = 0
    i = 0
    while i < len(gradeList):
        if gradeList[i] > specificValue:
            counter += 1
        i += 1
    return counter


initialGrade = validateGrade()

if initialGrade >= 80:
    print("Aprobado")
elif initialGrade >= 65 <80:
    print("Regular")
else:
    print("Reprobado")

grades = askGrades()
print(f"Tu promedio es: {calculateAverage(grades)}")


specificValue = float(input("Ingresa el valor para comparar las calificaciones: "))
cantidadMayores = countHigherGrades(grades, specificValue)
print(f"Hay {cantidadMayores} calificaciones mayores que {specificValue}")





