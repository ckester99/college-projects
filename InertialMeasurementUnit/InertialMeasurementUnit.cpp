#include <Wire.h>

class MPU6050{
  private:
  uint8_t address = 0x68;
  float accX, accY, accZ;
  float gyrX, gyrY, gyrZ;
  float temp;
  float outputs[3];
  float rawPitch, rawRoll, rawYaw; // from gyro
  float offGX, offGY, offGZ;
  float offAX, offAY, offAZ;
  float rawToOut = .3;
  float accPitch,accRoll,accYaw,accMag;
  float DT;
  
  
  public:
  void MP6050(uint8_t adr, DT =50 ){
    address =adr;
    Wire.beginTransmission(address);
    Wire.write(0x1B); //gyro then accelerometer config
    Wire.write(0x00); //gyro default settings +-250 deg/s
    Wire.write(0x08); //acc +- 4g
    Wire.endTransmission;
  }
  
  void calibrate(int sumTote = 500){
    float sumGX=0,sumGY=0,sumGZ=0;
    float sumAX=0,sumAY=0,sumAZ=0;
    
    for (int i=0,i<sumTote,i++){
      Wire.beginTransmission(address);
      Wire.write(0x3B);
      Wire.endTransmission(false);
      Wire.requestFrom(address,14);
      sumAX += (Wire.read() << 8 | Wire.read())/8192;
      sumAY += (Wire.read() << 8 | Wire.read())/8192;
      sumAZ += (Wire.read() << 8 | Wire.read())/8192;
      temp = (Wire.read() << 8 | Wire.read())*36.53;
      sumGX += (Wire.read() << 8 | Wire.read())/131;
      sumGY += (Wire.read() << 8 | Wire.read())/131;
      sumGZ += (Wire.read() << 8 | Wire.read())/131;
      delay(3);
    }
    offAX = sumAX/sumTote;
    offAY = sumAY/sumTote;
    offAZ = sumAZ/sumTote;
    offGX = sumGX/sumTote;
    offGY = sumGY/sumTote;
    offGZ = sumGZ/sumTote;
  }
  
  void update(){
    Wire.beginTransmission(address);
    Wire.write(0x3B)
    Wire.endTransmission(false);
    Wire.requestFrom(address,14);
    accX = (Wire.read() << 8 | Wire.read())/8192 - offAX;
    accY = (Wire.read() << 8 | Wire.read())/8192 - offAY;
    accZ = (Wire.read() << 8 | Wire.read())/8192 - offAZ;
    temp = (Wire.read() << 8 | Wire.read())*36.53;
    gyrX = (Wire.read() << 8 | Wire.read())/131 - offGX;
    gyrY = (Wire.read() << 8 | Wire.read())/131 - offGY;
    gyrZ = (Wire.read() << 8 | Wire.read())/131 - offGZ;
    
    rawPitch += (gyrY-rawRoll)*sin(rawYaw*PI/180) + (gyrX-rawPitch)*cos(rawYaw*PI/180);
    rawRoll += (gyrZ-rawYaw)*sin(rawPitch*PI/180) + (gyrY-rawRoll)*cos(rawPitch*PI/180);
    rawYaw += (gyrX-rawPitch)*sin(rawRoll*PI/180) + (gyrZ-rawYaw)*cos(rawRoll*PI/180);
    
    accMag = sqrt(sq(accX)+sq(accY)+sq(accZ));
    accPitch = atan(AccY / sqrt(pow(AccX, 2) + pow(AccZ, 2))*180/pi;
    accRoll = atan(-1 * AccX / sqrt(pow(AccY, 2) + pow(AccZ, 2)) * 180 / PI);
    
    rawPitch = .95*rawPitch+.05*accPitch;
    rawRoll = .95*rawRoll + .05*accRoll;
    out[0] += (rawX - out[0])*rawToOut;
    out[1] += (rawY - out[1])*rawToOut;
    out[2] += (rawZ - out[2])*rawToOut;
  }
  
  void setDT(float dt){
      DT = dt;
  }
                    
  float * get(){
   return outputs; 
  }
}
