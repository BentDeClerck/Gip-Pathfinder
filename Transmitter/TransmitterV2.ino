#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#define led 12

RF24 radio(7, 8); // CE, CSN
const byte addresses[][6] = {"00001", "00002"};

char buf[16];
String text;

String stationary= "0,0,0,0,0,0";
String forward = "150,0,1,1,0,150";
String backward = "150,1,0,0,1,150";
String right = "150,1,0,1,0,150";
String left = "150,0,1,0,1,150";

void setup() {
  Serial.begin(115200);
  Serial.println(radio.begin());
  radio.openWritingPipe(addresses[1]); // 00001
  radio.setPALevel(RF24_PA_MIN);
  
}


void loop() {
  delay(100);
  
  if (Serial.available() > 2) {
    text = Serial.readStringUntil('\n');
    Serial.println(text);
    text.toCharArray(buf, text.length()+1);
    
  }
  
  
  if(radio.write(buf, sizeof(buf))){
    Serial.println("SENDING " + String(buf));
  }
  else{
    Serial.println("FAILED SENDING " + String(buf));
  }
  memset(buf, 0, sizeof(buf));
}