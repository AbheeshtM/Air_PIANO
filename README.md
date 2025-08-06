# 🎹 Air Piano with Ultrasonic Sensors

Turn the air into a musical instrument! This project lets you play soothing piano notes with simple hand gestures using **ultrasonic sensors**, an **Arduino Uno**, and a **laptop or DFPlayer Mini** for sound output.

> Play music without touching anything — just wave your hands above 7 invisible keys!

---

## 📦 Components Used

| Component           | Quantity | Description                             |
|--------------------|----------|-----------------------------------------|
| Arduino Uno        | 1        | Microcontroller board                   |
| HC-SR04 Sensors    | 7        | For detecting hand distance             |
| USB Cable          | 1        | To connect Arduino to PC                |
| Laptop / PC        | 1        | To play sound using Python & Pygame     |
| Jumper Wires       | 20+      | For sensor connections                  |
| (Optional) DFPlayer Mini | 1   | For standalone sound output via Arduino |

---

## 🧠 How It Works

- Each **ultrasonic sensor** acts like a piano key.
- Sensors detect hand distance (e.g., <15 cm).
- Arduino sends a signal (`N1` to `N7`) via serial when a sensor is triggered.
- A Python script on the PC reads this and plays the corresponding `.wav` note using **Pygame**.

---

## 🖥️ Folder Structure

air-piano/
│
├── note/ # Folder with audio notes
│ ├── 0001.wav
│ ├── 0002.wav
│ └── ... up to 0007.wav
│
├── air_piano.py # Python script to run on PC
├── arduino_piano.ino # Arduino code
├── README.md

---

## 🚀 Getting Started

### 🛠️ Hardware Setup

1. **Connect 7 ultrasonic sensors** with:
   - All sensors sharing **Trigger Pin: D8**
   - Echo pins connected to: `D9, D3, D5, D7, D11, D10, D13`
2. Upload the Arduino code: [`arduino_piano.ino`](arduino_piano.ino)

### 🧑‍💻 Software Setup

1. **Install Python dependencies:**
   ```bash
   pip install pyserial pygame
Place sound files (0001.wav to 0007.wav) in the note/ folder. Use soft piano tones or pentatonic scale for better harmony.

Update Serial Port in air_piano.py:

SERIAL_PORT = 'COM3'  # Change as per your system
Run the Python script:
python air_piano.py
📷 Demo Screenshot


🎯 Features
✋ Touchless gesture-based musical interaction

🎶 Soothing note playback with randomized volume

⏱️ Built-in cooldown/debounce to prevent note spamming

🧩 Modular design — easy to add lights, DFPlayer, or MIDI output

📚 Educational Value
Learn about ultrasonic distance sensing

Work with Serial communication between Arduino and Python

Understand sound generation and gesture control systems

Great for STEM demos, science fairs, or music tech projects

📝 License
MIT License — free to use, share, and build upon.

