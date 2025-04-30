#se declara la variable y se le asigna el tipo
initial_grade: float
grades: list[float]
specific_value: float
grade: float

#esta función válida la calificación que se ingresa, primero válida que coincida el tipo de dato, tambien válida que
#se encuentre dentro del rango establecido
def validate_grade(message):
    valid_input:bool = False
    value:float = 0
    while not valid_input:
        try:
            value = float(input(message))
            if 0 <= value <= 100:  # Rango valido
                valid_input = True
            else:
                print("Valor erróneo, ingresa una calificación entre 0 y 100")
        except ValueError:
            print("ingresa una calificación valida (debe ser un numérica)")
    return value

#calcula el promedio de las calificaciones
def calculate_average(grade_list: list[float]):
    sum_grades = 0
    for element in grade_list:
        sum_grades += element
    return sum_grades / len(grade_list)

#solicita las calificaciones
def ask_grades():
    valid_input:bool = False
    grade_list:list[float] = []
    while not valid_input:
        try:            
            grades_input = input('Ingresa maximo 5 calificaciones separadas por coma (ejemplo: 85,90,78,96,88): ')
            grade_list = [float(x.strip()) for x in grades_input.split(",")]
            grade_list = [x for x in grade_list if 0 <= x <= 100]

            # Validar que haya calificaciones válidas
            if len(grade_list) == 0:
                print("No se han ingresado calificaciones válidas. Por favor, intente nuevamente.")
                continue
            # Validar que no supere las 5 calificaciones
            if len(grade_list) > 5:
                print(
                    f"Error: Debe maximo 5 calificaciones válidas. Ingresaste {len(grade_list)} calificaciones válidas.")
                continue

            valid_input = True

        except ValueError:
            print("Error: Ingresa solo números separados por comas")

    return grade_list


def count_higher_grades(grade_list: list[float], value: float):
    counter = 0
    i = 0
    while i < len(grade_list):
        if grade_list[i] > value:
            counter += 1
        i += 1
    return counter

def match_grades(grade_list: list[float], value: float):
    counter:int = 0
    for element in grade_list:
        if element == value:
            counter += 1
    return counter


initial_grade = validate_grade("ingresa una calificación numerica (de 0 a 100): ")

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

match_value = match_grades(grades, specific_value)
print(f"Hay {match_value} calificaciones que coinciden con {specific_value}")
