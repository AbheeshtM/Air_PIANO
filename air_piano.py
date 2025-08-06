import serial
import pygame
import time
import os
import random

# === SETTINGS ===
SERIAL_PORT = 'COM3'
BAUD_RATE = 9600
NOTE_FOLDER = 'note'      # Folder with 0001.wav to 0007.wav
cooldown = 0.3             # seconds

# === Initialize Audio ===
pygame.mixer.init()
notes = {
    'N1': '0001.wav',
    'N2': '0002.wav',
    'N3': '0003.wav',
    'N4': '0004.wav',
    'N5': '0005.wav',
    'N6': '0006.wav',
    'N7': '0007.wav'
}
note_last_played = {}

# === Connect to Arduino ===
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    print(f"✅ Connected to {SERIAL_PORT}. Waiting for notes...")
except Exception as e:
    print(f"❌ Could not open serial port: {e}")
    exit()

# === Main Loop ===
try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            current_time = time.time()

            if line in notes:
                # Debounce note
                if line not in note_last_played or (current_time - note_last_played[line]) > cooldown:
                    filepath = os.path.join(NOTE_FOLDER, notes[line])
                    if os.path.exists(filepath):
                        sound = pygame.mixer.Sound(filepath)
                        sound.set_volume(random.uniform(0.6, 0.9))  # softer, varied volume
                        sound.play()
                        print(f"🎵 Soothing note: {notes[line]}")
                        note_last_played[line] = current_time
                    else:
                        print(f"⚠️ File not found: {filepath}")
except KeyboardInterrupt:
    print("🛑 Exiting gracefully...")
    ser.close()
    pygame.quit()
