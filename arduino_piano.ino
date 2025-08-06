const int triggerPin = 8; // ✅ Updated trigger pin
const int echoPins[7] = {9, 3, 5, 7, 11, 10, 13};
const int threshold = 15; // cm

void setup() {
  Serial.begin(9600);
  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW); // Ensure LOW initially

  for (int i = 0; i < 7; i++) {
    pinMode(echoPins[i], INPUT);
  }
}

void loop() {
  for (int i = 0; i < 7; i++) {
    long duration, distance;

    // Trigger shared pin
    digitalWrite(triggerPin, LOW);
    delayMicroseconds(2);
    digitalWrite(triggerPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(triggerPin, LOW);

    // Read echo for current sensor
    duration = pulseIn(echoPins[i], HIGH, 30000); // timeout to avoid lock
    distance = duration * 0.034 / 2;

    if (distance > 0 && distance < threshold) {
      Serial.print("N");
      Serial.println(i + 1);  // Send N1–N7
    }

    delay(50); // slight gap between sensor checks
  }

  delay(100); // wait before next full scan
}