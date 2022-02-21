#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

int EnableA = 10;
int MotorA1 = 2;
int MotorA2 = 3;

int EnableB = 9;
int MotorB1 = 4;
int MotorB2 = 5;
 
RF24 radio(7, 8); // CE, CSN

const byte address[6] = "00001";

void setup() {
  Serial.begin(9600);
  pinMode(EnableA, OUTPUT);
  pinMode(EnableB, OUTPUT);
  pinMode(MotorA1, OUTPUT);
  pinMode(MotorA2, OUTPUT);
  pinMode(MotorB1, OUTPUT);
  pinMode(MotorB2, OUTPUT);
  
  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
}

void loop() {
  analogWrite(EnableA, HIGH);
  analogWrite(EnableB, HIGH);
  digitalWrite(MotorA2, LOW);  
  digitalWrite(MotorA1, HIGH);
  
  const char text[] = "Hello World";
  radio.write(&text, sizeof(text));
  Serial.println("Done");
  delay(1);
}
