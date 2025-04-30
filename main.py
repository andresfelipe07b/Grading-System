#se declara la variable y se le asigna el tipo
initial_grade: float
grades: list[float]
grade: float
specific_value: float

#esta función válida la calificación que se ingresa, primero válida que coincida el tipo de dato, tambien válida que
#se encuentre dentro del rango establecido
def validate_grade():
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
def calculate_average(grade_list: list[float]):
    sum = 0
    for grade in grade_list:
        sum += grade
    return sum / len(grade_list)

#solicita las calificaciones
def ask_grades():
    grade_list = []
    for i in range(5):
        grade = input(f"Ingresa la calificacion {i+1}:")
        grade_list.append(float(grade))
    return grade_list

def count_higher_grades(grade_list: list[float], value: float):
    counter = 0
    i = 0
    while i < len(grade_list):
        if grade_list[i] > value:
            counter += 1
        i += 1
    return counter


initial_grade = validate_grade()

if initial_grade >= 80:
    print("Aprobado")
elif initial_grade >= 65 <80:
    print("Regular")
else:
    print("Reprobado")

grades = ask_grades()
print(f"Tu promedio es: {calculate_average(grades)}")


specific_value = float(input("Ingresa el valor para comparar las calificaciones: "))
cantidad_mayores = count_higher_grades(grades, specific_value)
print(f"Hay {cantidad_mayores} calificaciones mayores que {specific_value}")
