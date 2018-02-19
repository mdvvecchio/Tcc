#include <string.h>
#include <Arduino.h>

String record = "A:100:1";
char *p, *i, *a, *b;

int LED = 13;
int FRENTE = 6;
int TRAZ = 5;
int MOTOR = 11;


void setup() {

  Serial.begin(9600);

  pinMode(LED, OUTPUT);
  pinMode(FRENTE, OUTPUT);
  pinMode(TRAZ, OUTPUT);
  pinMode(MOTOR, OUTPUT);

}

void loop () {

  if(Serial.available()>0)
  {
    record = Serial.readString();

    char charBuf[10];
    record.toCharArray(charBuf, 10);

    if(record != NULL) {

      //First strtok iteration
      p = strtok_r(charBuf,":",&i);
      a = strtok_r(NULL,":",&i);
      b = strtok_r(NULL,":",&i);

      if(String(p) == "f") {

        acionamento(FRENTE,int(a),int(b));
        

      }

      else if(String(p) == "t") {
        
        acionamento(TRAZ,int(a),int(b));

      }
      
      else if(String(p) == "m") {
        
        acionamento(MOTOR,int(a),int(b));
        
      }
      else {
        
        Serial.println("Aguardando Comando");
        
      }


    }
    Serial.print("Porta: ");
    Serial.print(p);
    Serial.print(" Intensidade: ");
    Serial.print(a);
    Serial.print(" Sentido: ");
    Serial.print(b);
    Serial.print(" / "); 
    Serial.print(record);
    Serial.println(""); 
    Serial.println("--------------------");
  }

}

void acionamento(int porta,int intensidade, int sentido)
{
  if (sentido == 1) { 
    porta = porta -1; 
  }
  
  analogWrite(porta, intensidade);
  Serial.println("OK");
  delay(100);
}


