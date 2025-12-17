# Desktop Santa Shimeji 🎅

**Lonely and coding alone this Christmas? Look no further!**

This is a Python-based desktop pet (Shimeji) that roams the bottom of your screen while you work. It features a frameless, transparent window that stays on top of your other applications, keeping you company during those long coding sessions.

## 🌟 Features
- **Transparent Background:** Uses Windows color keying for a seamless "sticker" look.
- **Taskbar Roaming:** Santa spawns and walks randomly along the bottom of the screen (on top of the taskbar).
- **Customizable:** Speed, size, and spawn location can be tweaked via a config file.
- **Modular Design:** Code is structured using Separation of Concerns (Logic, View, and Configuration).
- **Interactive Physics:** Drag and drop Santa anywhere on the screen.
- **Gravity Engine:** Santa automatically falls back to the taskbar when released.

## 📂 Project Structure
```text
SANTA_SHIMEJI/
├── src/
│   ├── main.py        # Application entry point
│   ├── config.py      # Settings (Speed, Size, Offsets)
│   ├── santa.py       # Main Controller
│   ├── behavior.py    # Logic/Model (Calculates movements)
│   ├── animation.py   # View (Handles GIF loading/cycling)
│   └── assets/        # Visual assets
└── README.md
```
🚀 How to Run
Prerequisites
Python 3.x installed (Make sure to check "Add to PATH" during installation).

Installation
1. Clone this repository:
```Bash
git clone [https://github.com/lemongoreng/desktop-santa-shimeji.git](https://github.com/lemongoreng/desktop-santa-shimeji.git)
```
2. Navigate to the project folder:
```Bash

cd desktop-santa-shimeji
```
3. Run the application:
```Bash

python src/main.py
```

⚙️ ConfigurationYou can customize Santa's behavior by editing src/config.py:
| Variable | Description | Default |
| :--- | :--- | :--- |
| `SPEED` | How many pixels he moves per update. | `1` (Slow) |
| `SCALE_FACTOR` | Resizes the GIF (Higher = Smaller). | `4` |
| `BOTTOM_OFFSET` | Pixel distance from the bottom of the screen. | `40` |

🎮 Controls
- **Right-Click Santa:** Close the application immediately.
- **Ctrl+C (Terminal):** Force stop the script if running from the command line.

🛠️ Technologies Used
- **Python:** Core programming language.
- **Tkinter:** GUI toolkit for window management.
- **MVC Pattern:** Code separated into Behavior (Model), Animation (View), and Controller.
