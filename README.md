# 🗺️ Guess The U.S. State Game

This is a fun and interactive Python game built using the `turtle` graphics library and `pandas`. The goal is to guess all 50 U.S. states. Each correct guess will display the state name on a blank U.S. map.


---

## 🚀 How It Works

- The game displays a blank U.S. map.
- You're prompted to guess a state name.
- If correct, the state's name appears in its correct location on the map.
- The game continues until all 50 states are guessed or you type `Exit`.
- A file named `Unanswered.csv` is created with the states you missed.

---

## 📦 Requirements

- Python 3.x
- `pandas` library
- `turtle` (comes with Python)
- `50_states.csv` (CSV file with state names and coordinates)
- `blank_states_img.gif` (U.S. map image)

---

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone git@github.com:ekamcodes/Guess-The-US-State.git
   cd Guess-The-US-State
   ```

2. Make sure `pandas` is installed:
   ```bash
   pip install pandas
   ```

3. Run the Python file:
   ```bash
   python main.py
   ```

---

## 📁 File Structure

```
.
├── main.py
├── 50_states.csv
├── blank_states_img.gif
├── Unanswered.csv      # (Generated after gameplay)
└── README.md
```

---

## 🧠 Educational Purpose

This game was built as a part of learning Python, data handling with `pandas`, and graphical rendering with `turtle`.

---

## ✨ Author

Made with ❤️ by [Ekamjot Singh](https://github.com/ekamcodes)
