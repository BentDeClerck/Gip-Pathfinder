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
const int MotorB2 = A0;

const int EnableC = 5;
const int MotorC1 = A2;
const int MotorC2 = A3;

const int EnableD = 6;
const int MotorD1 = A4;
const int MotorD2 = A5;

int values[12] = {0,0,0,0,0,0,0,0,0,0,0,0};
String waarde = "";

String stationary= "0,0,0,0,0,0";
String forward = "150,0,1,1,0,150";
String backward = "150,1,0,0,1,150";
String right = "150,1,0,1,0,150";
String left = "150,0,1,0,1,150";



void setup() {
  pinMode(EnableA, OUTPUT);
  pinMode(EnableB, OUTPUT);
  pinMode(EnableC, OUTPUT);
  pinMode(EnableD, OUTPUT);
  
  pinMode(MotorA1, OUTPUT);
  pinMode(MotorA2, OUTPUT);
  
  pinMode(MotorB1, OUTPUT);
  pinMode(MotorB2, OUTPUT);

  pinMode(MotorC1, OUTPUT);
  pinMode(MotorC2, OUTPUT);
  
  pinMode(MotorD1, OUTPUT);
  pinMode(MotorD2, OUTPUT); 
  
  radio.begin();
  radio.openReadingPipe(1, addresses[1]); // 00001
  radio.setPALevel(RF24_PA_MIN);
  Serial.begin(115200);
  radio.startListening();
}


void loop() {
  values[0] = 0; values[1] = 0; values[2] = 0; values[3] = 0; values[4] = 0; values[5] = 0; values[6] = 0; values[7] = 0; values[8] = 0; values[9] = 0; values[10] = 0; values[11] = 0;
  
  analogWrite(EnableA, values[0]); analogWrite(EnableB, values[5]); digitalWrite(MotorA2, values[2]); digitalWrite(MotorA1, values[1]); digitalWrite(MotorB2, values[4]); digitalWrite(MotorB1, values[3]); 
  analogWrite(EnableC, values[6]); analogWrite(EnableD, values[11]); digitalWrite(MotorC2, values[8]); digitalWrite(MotorC1, values[7]); digitalWrite(MotorD2, values[10]);   digitalWrite(MotorD1, values[9]);
  
  if ( radio.available()) {
    
    char text[16] = "";
    radio.stopListening();
    radio.read(&text, sizeof(text));
    
    Serial.println(String(text));
    Serial.println(strlen(text));
    
    for (int i=0; i<strlen(text);i++){
      Serial.println(text[i]);
      
      
      if (String(text[i]) == "1") {
        values[0] = 150; values[1] = 0; values[2] = 1; values[3] = 1; values[4] = 0; values[5] = 150; values[6] = 150; values[7] = 0; values[8] = 1; values[9] = 1; values[10] = 0; values[11] = 150;
        analogWrite(EnableA, values[0]); analogWrite(EnableB, values[5]); digitalWrite(MotorA2, values[2]); digitalWrite(MotorA1, values[1]); digitalWrite(MotorB2, values[4]);   digitalWrite(MotorB1, values[3]);
        analogWrite(EnableC, values[6]); analogWrite(EnableD, values[11]); digitalWrite(MotorC2, values[8]); digitalWrite(MotorC1, values[7]); digitalWrite(MotorD2, values[10]);   digitalWrite(MotorD1, values[9]);
      }
      if (String(text[i]) == "2"){
        values[0] = 150; values[1] = 1; values[2] = 0; values[3] = 0; values[4] = 1; values[5] = 150; values[6] = 150; values[7] = 1; values[8] = 0; values[9] = 0; values[10] = 1; values[11] = 150;
        analogWrite(EnableA, values[0]); analogWrite(EnableB, values[5]); digitalWrite(MotorA2, values[2]); digitalWrite(MotorA1, values[1]); digitalWrite(MotorB2, values[4]);   digitalWrite(MotorB1, values[3]);
        analogWrite(EnableC, values[6]); analogWrite(EnableD, values[11]); digitalWrite(MotorC2, values[8]); digitalWrite(MotorC1, values[7]); digitalWrite(MotorD2, values[10]);   digitalWrite(MotorD1, values[9]);
      }
      
      if (String(text[i]) == "3"){
        values[0] = 150; values[1] = 0; values[2] = 1; values[3] = 0; values[4] = 0; values[5] = 0; values[6] = 150; values[7] = 1; values[8] = 0; values[9] = 0; values[10] = 0; values[11] = 0;
        analogWrite(EnableA, values[0]); analogWrite(EnableB, values[5]); digitalWrite(MotorA2, values[2]); digitalWrite(MotorA1, values[1]); digitalWrite(MotorB2, values[4]);   digitalWrite(MotorB1, values[3]);
        analogWrite(EnableC, values[6]); analogWrite(EnableD, values[11]); digitalWrite(MotorC2, values[8]); digitalWrite(MotorC1, values[7]); digitalWrite(MotorD2, values[10]);   digitalWrite(MotorD1, values[9]);
      }
      
     
      delay(1000);
    }
   
        
   radio.startListening();
   // eens de while loop weg doen, weet niet goed wat die doet
  }
  delay(100);
  
}
