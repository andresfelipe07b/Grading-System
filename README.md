# 📊 Sistema de calificaciones

## 📘 English version
[Click here to see the README in english version](README.en.md)

Este proyecto en Python permite validar, analizar y clasificar calificaciones numéricas ingresadas por el usuario. Se enfoca en prácticas de entrada de datos, validación, estructuras de control y funciones.

---

## 📌 Características

- Valida calificaciones individuales entre 0 y 100.
- Clasifica una calificación inicial como:
  - Aprobado (≥80)
  - Regular (65-79)
  - Reprobado (<65)
- Solicita hasta 5 calificaciones ingresadas en una sola línea.
- Calcula el promedio de las calificaciones válidas.
- Cuenta cuántas calificaciones son mayores o iguales a un valor específico.

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python 3
- **Estilo:** Tipado estático opcional (`variable: tipo`)
- **Funciones:** Bien documentadas con docstrings tipo `Google`/`Sphinx`

---

## ▶️ Cómo ejecutar el programa

1. Asegúrate de tener Python 3 instalado.
2. Descarga el archivo `.py` del repositorio.

```bash
git clone https://github.com/andresfelipe07b/Grading-System
cd Grading-System
```

3. Ejecuta el script en consola
4. Sigue las instrucciones en pantalla para ingresar las calificaciones.

---

## 💡 Posibles mejoras a futuro

- [ ] Mostrar resumen estadístico: calificación máxima, mínima y desviación estándar.
- [ ] Permitir al usuario elegir entre ingresar calificaciones una a una o por lote.
- [ ] Exportar los resultados a un archivo `.csv`.
- [ ] Crear pruebas unitarias para las funciones.
- [ ] Internacionalización: mensajes en otros idiomas.
- [ ] Interfaz gráfica.

---

## 📷 Ejemplo de uso

```
ingresa una calificación numerica (de 0 a 100): 78
Regular
Ingresa maximo 5 calificaciones separadas por coma (ejemplo: 85,90,78,96,88): 60,80,75,100,78
las calificaciones validas que ingresaste fueron: [60.0, 80.0, 75.0, 100.0, 78.0]
Tu promedio es: 78.6
ingresa una calificación numerica (de 0 a 100) para comparar con las calificaciones ingresadas: 78
Hay 2 calificaciones mayores que 78.0
Hay 1 calificaciones que coinciden con 78.0
```

---

## 🤝 Contribuciones

¿Tienes ideas para mejorar este evaluador? ¡Contribuye! Haz un fork del repositorio y envía un pull request con tus propuestas.
