# 📊 Grading System


This Python project allows users to validate, analyze, and classify numeric grades. It focuses on input handling, validation, control structures, and functions.

---

## 📌 Features

- Validates individual grades between 0 and 100.
- Classifies a single grade as:
  - Passed (≥80)
  - Regular (65–79)
  - Failed (<65)
- Accepts up to 5 grades in a single line.
- Calculates the average of valid grades.
- Counts how many grades are greater than or equal to a specified value.

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **Style:** Optional static typing (`variable: type`)
- **Functions:** Well-documented with `Google`/`Sphinx`-style docstrings

---

## ▶️ How to Run the Program

1. Make sure Python 3 is installed on your system.
2. Download the `.py` file from the repository.

```bash
git clone https://github.com/andresfelipe07b/Grading-System
cd Grading-System
```

3. Run the script in the terminal.
4. Follow the on-screen instructions to enter grades.

---

## 💡 Possible Future Improvements

- [ ] Show statistical summary: max, min, and standard deviation.
- [ ] Let users choose between single or batch input.
- [ ] Export results to a `.csv` file.
- [ ] Add unit tests for the functions.
- [ ] Internationalization: support for other languages.
- [ ] Graphical user interface.

---

## 📷 Example Usage

```
Enter a numeric grade (from 0 to 100): 78
Regular
Enter up to 5 grades separated by commas (e.g., 85,90,78,96,88): 60,80,75,100,78
Valid grades you entered: [60.0, 80.0, 75.0, 100.0, 78.0]
Your average is: 78.6
Enter a numeric grade (from 0 to 100) to compare with the entered grades: 78
There are 2 grades greater than 78.0
There is 1 grade equal to 78.0
```

---

## 🤝 Contributions

Have ideas to improve this evaluator? Contribute! Fork the repository and submit a pull request with your proposals.
