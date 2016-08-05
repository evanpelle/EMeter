/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

 This example code is in the public domain.
 */

#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
                // twelve servo objects can be created on most boards

int redLed = 7;
int greenLed = 6;


// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  myservo.attach(9);
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);

  if(sensorValue > 30) {
    digitalWrite(greenLed, LOW);
    digitalWrite(redLed, HIGH);
    myservo.write(25);
  } else {
    myservo.write(190);
    digitalWrite(greenLed, HIGH);
    digitalWrite(redLed, LOW);
  }
  // print out the value you read:
  Serial.println(sensorValue);
  delay(1);        // delay in between reads for stability
}


