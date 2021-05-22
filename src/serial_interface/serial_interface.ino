#include <AFMotor.h>

//initial motors pin
AF_DCMotor motor1(1, MOTOR12_1KHZ);
AF_DCMotor motor2(2, MOTOR12_1KHZ);
AF_DCMotor motor3(3, MOTOR34_1KHZ);
AF_DCMotor motor4(4, MOTOR34_1KHZ);
int myspeed = 255;

void setup() {
  Serial.begin(9600);
  
}
void loop() {
  if (Serial.available() > 0){
    int data = Serial.read();

    if (data == 119){
      fordward();    
    }
  
    else if(data== 118){
      Stop();
      }
      
    else if(data== 97){
      right();
      }  
    
    else if(data== 100){
      left();
      }  
     else if(data== 115){
      backward();
      }      

    else if(data== 122){
      left_back();
      }      
      
     else if(data== 120){
      right_back();
      }         
    }
 
delayMicroseconds(50);

}



void fordward()
{
 motor1.setSpeed(myspeed);
 motor1.run(FORWARD);
 
 motor2.setSpeed(myspeed);
 motor2.run(FORWARD); 

 motor3.setSpeed(myspeed);
 motor3.run(FORWARD);
  
 motor4.setSpeed(myspeed);
 motor4.run(FORWARD);
}

void backward()
{
 motor1.setSpeed(myspeed);
 motor1.run(BACKWARD);
 
 motor2.setSpeed(myspeed);
 motor2.run(BACKWARD); 

 motor3.setSpeed(myspeed);
 motor3.run(BACKWARD);
  
 motor4.setSpeed(myspeed);
 motor4.run(BACKWARD);
}

void right()
{
 motor1.setSpeed(myspeed);
 motor1.run(FORWARD);
 
 motor2.setSpeed(myspeed);
 motor2.run(RELEASE); 

 motor3.setSpeed(myspeed);
 motor3.run(RELEASE);
  
 motor4.setSpeed(myspeed);
 motor4.run(FORWARD);
}

void right_back()
{
 motor1.setSpeed(myspeed);
 motor1.run(BACKWARD);
 
 motor2.setSpeed(myspeed);
 motor2.run(RELEASE); 

 motor3.setSpeed(myspeed);
 motor3.run(RELEASE);
  
 motor4.setSpeed(myspeed);
 motor4.run(BACKWARD);
}
void left()
{
 motor1.setSpeed(myspeed);
 motor1.run(RELEASE);
 
 motor2.setSpeed(myspeed);
 motor2.run(FORWARD); 

 motor3.setSpeed(myspeed);
 motor3.run(FORWARD);
  
 motor4.setSpeed(myspeed);
 motor4.run(RELEASE);
}

void left_back()
{
 motor1.setSpeed(myspeed);
 motor1.run(RELEASE);
 
 motor2.setSpeed(myspeed);
 motor2.run(BACKWARD); 

 motor3.setSpeed(myspeed);
 motor3.run(BACKWARD);
  
 motor4.setSpeed(myspeed);
 motor4.run(RELEASE);
}


void Stop()
{
  motor1.setSpeed(0); //Define minimum velocity
  motor1.run(RELEASE); //stop the motor when release the button
  motor2.setSpeed(0); //Define minimum velocity
  motor2.run(RELEASE); //rotate the motor clockwise
  motor3.setSpeed(0); //Define minimum velocity
  motor3.run(RELEASE); //stop the motor when release the button
  motor4.setSpeed(0); //Define minimum velocity
  motor4.run(RELEASE); //stop the motor when release the button
}
