#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <Servo.h>
#define button 4
RF24 radio(7, 8); // CE, CSN

const byte addresses[][6] = {"00001", "00002"};

const int EnableA = 10;
const int MotorA1 = 2;
const int MotorA2 = 3;

const int EnableB = 9;
const int MotorB1 = 4;
const int MotorB2 = 5;


int values[6] = {0,0,0,0,0,0};


void setup() {
  pinMode(EnableA, OUTPUT);
  pinMode(EnableB, OUTPUT);
  pinMode(MotorA1, OUTPUT);
  pinMode(MotorA2, OUTPUT);
  pinMode(MotorB1, OUTPUT);
  pinMode(MotorB2, OUTPUT);
  
  radio.begin();
  radio.openReadingPipe(1, addresses[1]); // 00001
  radio.setPALevel(RF24_PA_MIN);
  Serial.begin(115200);
  radio.startListening();
}


void loop() {
  
  
  if ( radio.available()) {
    while (radio.available()) {
      char text[16] = "";
      radio.stopListening();
      radio.read(&text, sizeof(text));
      radio.startListening();
      Serial.println(text);


      char* pointer = strtok(text, ",");
      int i = 0;
      
      while (pointer != NULL) {
        String s = String(pointer);
        int a = s.toInt();
        
        values[i] = a; 
        Serial.println(values[i]);
        pointer = strtok(NULL, ",");
        i++;
      }
      analogWrite(EnableA, values[0]);
      analogWrite(EnableB, values[5]);
      digitalWrite(MotorA2, values[2]);  
      digitalWrite(MotorA1, values[1]);
      digitalWrite(MotorB2, values[4]);  
      digitalWrite(MotorB1, values[3]);
      
    }
   
  }
  delay(100);
}
