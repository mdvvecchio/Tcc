#include <string.h>
#include <Arduino.h>

String record = "A:100:1";
char *p, *i, *a, *b;

int FRENTE = 6;
int TRAZ = 5;
int MOTOR = 10;


void setup() {

  Serial.begin(9600);

  pinMode(FRENTE, OUTPUT);
  pinMode(TRAZ, OUTPUT);
  pinMode(MOTOR, OUTPUT);
  pinMode(9, OUTPUT); //Enable do motor acionado
  
  analogWrite(11, 0);
  analogWrite(10, 0);
  analogWrite(5, 0);
  analogWrite(6,0);
  digitalWrite(8,HIGH);

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

        acionamento(FRENTE,String(a).toInt(),0);
  Serial.println("****************");
  Serial.print("frente - ");
  Serial.print(a);
  Serial.print(" - ");
  Serial.println(b);
  Serial.println("****************");
      }

      else if(String(p) == "t") {

        acionamento(TRAZ,String(a).toInt(),0);
  Serial.println("****************");
  Serial.print("traz - ");
  Serial.print(int(a));
  Serial.print(" - ");
  Serial.println(b);
        Serial.println("****************");
      }

      else if(String(p) == "m") {

        acionamento(MOTOR,String(a).toInt(),String(b).toInt());
  Serial.println("****************");
  Serial.print("motor - ");
  Serial.print(int(a));
  Serial.print(" - ");
  Serial.println(b);
        Serial.println("****************");
      }
      else {
  Serial.println("****************");
        Serial.println("Aguardando Comando");
        Serial.println("****************");
      }

    }
    Serial.println("--------------------");
    Serial.print("Porta: ");
    Serial.print(p);
    Serial.print(" Intensidade: ");
    Serial.print(int(a));
    Serial.print(" Sentido: ");
    Serial.print(b);
    Serial.print(" / ");
    Serial.println(record);
    Serial.println("--------------------");
  }

}

void acionamento(int porta,int intensidade, int sentido)
{
  if(porta == 10 || porta == 11){
    analogWrite(11, 0);
    analogWrite(10, 0);
    delay(50);
  }
    
  if (sentido == 1) {
    porta = porta -1;
    Serial.println("inverte");
  }

  analogWrite(porta, intensidade);
  Serial.println("++++++++++++++++++++++++");
  Serial.print("OK");
  Serial.print(" - ");
  Serial.print(intensidade);
  Serial.print(" - ");
  Serial.println(porta);
  Serial.println("++++++++++++++++++++++++");
  delay(200);
}
