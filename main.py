# Declaración de variables globales con sus tipos
initial_grade: float  # Almacena la calificación inicial individual
grades: list[float]  # Lista para almacenar el conjunto de calificaciones
specific_value: float  # Valor de referencia para comparaciones
grade: float  # Variable auxiliar para manipulación de calificaciones



def validate_grade(message) -> float:
    """
        Válida que la calificación ingresada sea un número entre 0 y 100.

        Args:
            message (str): Mensaje que se mostrará al usuario al solicitar la entrada

        Returns:
            float: Calificación validada entre 0 y 100
        """
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

# Calcula el promedio de las calificaciones y lo retorna
def calculate_average(grade_list: list[float]) -> float:
    """
        Calcula el promedio de una lista de calificaciones.

        Args:
            grade_list (list[float]): Lista de calificaciones a promediar

        Returns:
            float: Promedio de las calificaciones
        """
    sum_grades = 0
    for element in grade_list:
        sum_grades += element
    return sum_grades / len(grade_list)

#solicita las calificaciones
def ask_grades() -> list[float]:
    """
       Solicita al usuario ingresar hasta 5 calificaciones separadas por comas.

       Returns:
           list[float]: Lista de calificaciones válidas (0-100)

       Notas:
           - Las calificaciones deben estar separadas por comas
           - Se aceptan máximo 5 calificaciones
           - Solo se consideran válidas las calificaciones entre 0 y 100
       """
    valid_input:bool = False
    grade_list:list[float] = []
    while not valid_input:
        try:            
            grades_input = input('Ingresa maximo 5 calificaciones separadas por coma (ejemplo: 85,90,78,96,88): ')
            grade_list = [
                float(x.strip())
                for x in grades_input.split(",")
                if x.strip() and not x.strip().endswith(',') # Verifica que no termine en coma
            ]
            grade_list = [x for x in grade_list if 0 <= x <= 100] # Filtra solo las calificaciones que estén dentro del rango
            print(f"las calificaciones validas que ingresaste fueron: {grade_list}")

            # Validar que haya calificaciones válidas
            if len(grade_list) == 0:
                print("No se han ingresado calificaciones válidas. Por favor, intente nuevamente.")
                continue
            # Validar que no supere las 5 calificaciones
            if len(grade_list) > 5:
                print(
                    f"Error: Deben ser maximo 5 calificaciones válidas. Ingresaste {len(grade_list)} calificaciones.")
                continue

            valid_input = True

        except ValueError:
            print("Error: Valor incorrecto. ingresa nuevamente las calificaciones separadas por coma: ")
            grade_list = []

    return grade_list


def count_higher_grades(grade_list: list[float], value: float) -> int:
    """
        Cuenta cuántas calificaciones son mayores que un valor específico.

        Args:
            grade_list (list[float]): Lista de calificaciones a comparar
            value (float): Valor de referencia para la comparación

        Returns:
            int: Número de calificaciones mayores que el valor de referencia
        """
    counter = 0
    i = 0
    while i < len(grade_list):
        if grade_list[i] > value:
            counter += 1
        i += 1
    return counter

def match_grades(grade_list: list[float], value: float) -> int:
    """
    Cuenta cuántas calificaciones son iguales a un valor específico.

    Args:
        grade_list (list[float]): Lista de calificaciones a comparar
        value (float): Valor a buscar en la lista

    Returns:
        int: Número de calificaciones que coinciden exactamente con el valor
    """
    counter: int = 0
    for element in grade_list:
        if element != value:
            continue  # Salta a la siguiente iteración si no hay coincidencia
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

specific_value = validate_grade("ingresa una calificación numerica (de 0 a 100) para comparar con las calificaciones ingresadas: ")
cantidad_mayores = count_higher_grades(grades, specific_value)
print(f"Hay {cantidad_mayores} calificaciones mayores que {specific_value}")

match_value = match_grades(grades, specific_value)
print(f"Hay {match_value} calificaciones que coinciden con {specific_value}")

print("prueba")
