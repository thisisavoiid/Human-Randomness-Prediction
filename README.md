Human Randomness Prediction

A console-based Python number prediction tool. Tracks user input sequences and predicts the next number based on patterns.

---

## Features

- Enter numbers between 1-9
- Tracks all user entries and stores them in `dataset.json`
- Predicts next number using the last 2 numbers from previous sequences
- Displays prediction success rate
- Stores sequences of last 3 entries for pattern analysis
- Reset dataset option (irreversible)
- Animated ASCII art greeting and interactive menu
- Real-time feedback on prediction accuracy

---

## How to Use

1. Run the program:
```bash
python <script_name>.py
````

2. Choose from the menu:

   * Start the prediction model
   * Read dataset stats (WIP)
   * Reset dataset
3. Enter numbers (1-9) one at a time.
4. See prediction results and success rate after each entry.

---

## Requirements

* Python 3.x
* `dataset.json` file in the same directory:

```json
{
  "total_guesses": 0,
  "total_correct": 0,
  "userchoices": [],
  "userchoices_chunks": [],
  "number_counter": {}
}
```

---

## Notes

* Predictions are based only on previous input patterns.
* Dataset updates automatically after each guess.
* Resetting the dataset is irreversible.
* Works best after multiple inputs to build prediction accuracy.


