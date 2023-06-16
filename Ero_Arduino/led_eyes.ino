#include "LedControl.h"

/*
 pin 2 is connected to the DataIn 
 pin 4 is connected to the CLK 
 pin 3 is connected to LOAD 
 ***** Please set the number of devices you have *****
 */
//LedControl lc=LedControl(2,4,3,2);
#define NBR_MTX 2
LedControl lc=LedControl(2,3,4, NBR_MTX);
const int addrL = 0;  // first LED matrix - Left robot eye
const int addrR = 1;  // second LED matrix - Right robot eye
byte left[8];
void setup() {
  /*The MAX72XX is in power-saving mode on startup*/
  lc.shutdown(addrL,false);
  lc.shutdown(addrR,false);
  /* Set the brightness*/
  lc.setIntensity(addrL,1);
  lc.setIntensity(addrR,1);
  /* and clear the display */
  lc.clearDisplay(addrL);
  lc.clearDisplay(addrR);

  // turn on all LEDs for a test
  for(int row=0;row<8;row++) {
    lc.setRow(addrL, row, 255);
    lc.setRow(addrR, row, 255);
    delay(100);
  }
  delay(300);
}

void showNeutral() {
byte left[8] = {
B00000000,
B00111100,
B01000010,
B01011010,
B01011010,
B01000010,
B00111100,
B00000000};

  displayEmotion(left, left);
}

void showblink() {
  byte left[8]= {B00000000,B01111110,B10000001,B10001101,B10001101,B10000001,B01111110,B00000000};displayEmotion(left, left);}
void showblink_1() {  
  byte left[8]= {B00000000,B00111110,B01000001,B01001101,B01001101,B01000001,B00111110,B00000000};displayEmotion(left, left);}
void showblink_2() {   
  byte left[8] ={B00000000,B00011110,B00100001,B00101101,B00101101,B00100001,B00011110,B00000000};displayEmotion(left, left);}
void showblink_3() {   
  byte left[8] ={B00000000,B00001100,B00010010,B00011110,B00011110,B00010010,B00001100,B00000000};displayEmotion(left, left);}
void showblink_4() {   
  byte left[8] ={B00000000,B00000100,B00001010,B00001110,B00001110,B00001010,B00000100,B00000000};displayEmotion(left, left);}  
void showblink_5() {   
  byte left[8] ={B00000000,B00000100,B00000110,B00000110,B00000110,B00000110,B00000100,B00000000};displayEmotion(left, left);}  


void displayEmotion(byte left[8], byte right[8]) {
  lc.clearDisplay(addrL);
  lc.clearDisplay(addrR);
  for(int row=0;row<8;row++) {
    lc.setRow(addrL,row,left[row]);
    lc.setRow(addrR,row,right[row]);
  }
}

void loop() {
  showblink();
  delay(4000);

  showblink_1();
  delay(100);
  showblink_2();
  delay(100);
  showblink_3();
  delay(100);
  showblink_4();
  delay(100);
  showblink_5();
  delay(200);
  showblink_4();
  delay(100);
  showblink_3();
  delay(100);
  showblink_2();
  delay(100);
  showblink_1();
  delay(100);
  showblink();
  
}
