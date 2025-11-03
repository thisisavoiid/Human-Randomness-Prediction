# Human-Randomness-Prediction

A **Python console-based number prediction tool** that learns from user inputs. The program collects sequences of numbers between 1-9, predicts future inputs based on historical patterns, and keeps track of prediction accuracy. It uses JSON to persist the dataset between runs.

---

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Mechanics & Design](#mechanics--design)
- [Author](#author)

---

## Features

- Tracks **user number inputs** and sequences.
- Predicts the next number based on previous patterns.
- Maintains **success rate** and prediction statistics.
- Saves collected data to a JSON file (`dataset.json`) for persistence.
- Reset option for the dataset.
- Console-based **ASCII art UI** for a fun visual touch.

---

## Usage

1. Run the program:
```bash
python main.py
````

2. Select an option from the menu:

   * **Start the model** – begin entering numbers (1–9) and see predictions in real-time.
   * **Read dataset stats (WIP)** – view collected data and model accuracy (work in progress).
   * **Reset dataset** – clear all historical data.
3. Enter numbers as prompted. The program predicts your next input based on historical patterns.
4. View the **success rate** after each prediction.
5. Exit anytime by closing the console window.

> Animated ASCII art and typewriter-style text enhance the interactive experience.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/thisisavoiid/Human-Randomness-Prediction.git
```

2. Navigate into the project folder:

```bash
cd Human-Randomness-Prediction
```

3. Make sure you are using **Python 3.x**.
4. Run the program:

```bash
python predict.py
```

---

## Mechanics & Design

* **Data Storage**:

  * Uses a JSON file (`dataset.json`) to store:

    * `total_guesses` – total inputs by the user.
    * `total_correct` – correct predictions made.
    * `userchoices` – full list of user inputs.
    * `userchoices_chunks` – sequences of 3 numbers for prediction.
    * `number_counter` – count of individual numbers entered.
* **Prediction Algorithm**:

  * Tracks sequences of 3 numbers.
  * Predicts the next number if the first two numbers match a previous sequence.
  * Calculates and displays prediction success rate.
* **Console UI**:

  * Uses ASCII art for a visual header.
  * Typewriter-style display for greetings and instructions.
  * Clears screen between inputs for a dynamic experience.
* **Reset Function**:

  * Allows complete reset of the dataset with user confirmation.

---

## Author

**Jonathan Huber** – Developed as a console-based Python prediction tool.

---

> Made with ❤️ in Python
