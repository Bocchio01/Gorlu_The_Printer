#include <Servo.h>
#include <AFMotor.h>

//declare servo and motors obj
Servo Pen;
AF_Stepper MotorX(48, 1);
AF_Stepper MotorY(48, 2);

int i, controll = 0, pen_up = -1, pen_down = -1;
float previous_x = 0, previous_y = 0, next_x, next_y;
char pen_position, dir_x, dir_y;

void setup()
{
  Serial.begin(9600);

  Pen.attach(9);
  Pen.write(155);

  MotorX.setSpeed(600);
  MotorY.setSpeed(600);
}

void loop()
{
  while (1)
  {
    while (Serial.available() > 0)
    {
      //get servo position for pen_up and pen_down
      if (pen_up == -1)
      {
        pen_down = Serial.parseInt();
        pen_up = Serial.parseInt();
      }

      //get data of next movement to do
      pen_position = Serial.read();
      next_x = Serial.parseInt();
      next_y = Serial.parseInt();
      Serial.read();

      //set Pen_position
      if (pen_position == 'U')
      {
        Pen.write(pen_down);
        controll = 1;
        delay(50);
      }
      else
      {
        Pen.write(pen_up);
      }

      //analyze coordinates in complace to the previous
      dir_x = previous_x < next_x ? FORWARD : BACKWARD;
      dir_y = previous_y < next_y ? FORWARD : BACKWARD;

      //send data to MotorX/Y
      for (i = 0; i < abs(next_x - previous_x); i++)
      {
        MotorX.onestep(dir_x, DOUBLE);
        delay(5);
      }
      
      for (i = 0; i < abs(next_y - previous_y); i++)
      {
        MotorY.onestep(dir_y, DOUBLE);
        delay(5);
      }

      //update old coordinates with the current one
      previous_x = next_x;
      previous_y = next_y;

      //to avoid problems with Motor overheating
      MotorX.release();
      MotorY.release();

      //if Pen_position = up, Arduino send letter A to main application data_sender
      //in order to avoid data overlap
      if (controll == 1)
      {
        Serial.print("A");
        controll = 0;
      }
    }
  }
}
