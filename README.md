# SST IoT Development Board Experiments Using MicroPython

| **Python Installation Guide** |
| :---------- |
|[Click Here](Python-Installation.md)|

-----------------

| **Microsoft Visual C++ 2010** |
| :------------ |
[Click Here](Visual)

-------------------------

| **Installation of uPycraft IDE** |
| :------------ |
[Click Here](uPycraft-Installation.md)

-------------------


| **Flash/Upload MicroPython Firmware to ESP32** |
| :------------ |
[Click Here](Flash.md)

-------------------------

## SST IoT Development Board Pin Description

| **Components** | **GPIO PIN DESCRIPTION** |
|:----:|:----:|
|Buzzer | 14 |
|Bluetooth| RX - 16, TX - 17 |
| DHT 11| 32 |
| DC Motor | M1 - 25/33, M2 - 26/27|
| LCD | SCL - 22, SDA - 21 |
| ON Board LED | 02 |
| OLED | SCL - 22, SDA - 21 |
| RGB LED | 4 |
| RELAY | 13 |
| Servo Motor | S1 - 12, S2 - 2, S3 - 15|
| SD CARD | CS - 5, SCK - 18, MOSI - 23, MISO - 19 | 
| UART 0 | TX0 - 01, RX0 - 03 |

| **Components** | **GPIN PIN DESCRIPTION** |
|:----:|:----:|
|POT | 34 |
|PUSH BUTTON | 35 |
|LDR | 36 |
|Thermister | 39 |

|**ISOLATED IO PINS** | **J19** | **J14** | 
|:----:|:----:| :-----: | 
| | GPIO18 |GPIO3| 
| |GPIO19 |GPIO2 |
| |GPIO23 |GPIO1 |
| |GPIO25 | GPIO4| 
|| GPIO26 | GPIO5 |
|| GPIO27 | GPIO12 |
|| GPIO32 | GPIO13 |
|| GPIO33 | GPIO14 |
|| GPIO34 | GPIO15 |
|| GPIO36 | GPIO16 |
|| GPIO39 | GPIO17 |


| **Analog Inputs (ADC)** | GPIO4 |GPIO2 | GPIO15 |GPIO13 | GPIO12 |
|:----:|:----:| :-----: | :------: | :-----: | :---------: |
| |GPIO14 |GPIO27 | GPIO26 | GPIO25 | GPIO33 |
| |GPIO32 |GPIO35 |GPIO34 |GPIO39 | GPIO36 |


-----------------

### List of Experiments

| **No** | **Experiment Name** | 
| :---: | :---       |
|1|Program to OnBoard blink LED |
|2| Program to blink External LED |
|3|Program to Control LED using Button |
|4| Program for Boot Button LED |
|5|Program to Get input from two switches and switch on corresponding LEDs.|
|6|Program to Flash an LED at a given on time and off time cycle, where the two times are taken from a file.|
|7|Program to read Buntton 35 |
|8|Program to Switch on a relay at a given time using sleep function, where the relay’s contact terminals are connected to a load.|
|9|Program for Buzzer |
|10|Program for Thermistor|
|11|Program for Light Dependent Resistor(LDR)|
|12|Program for I2C LCD Scan |
|13| Program for I2C LCD Display |
|14|Implement an intruder system that sends an alert to the given email|
|15|Control Relay Module with MicroPython Web Server|
|16| Program for Smoke Sensor |
|17|Program for Reaction Game - Single  |
|18|Traffic Light  |
|19| Traffic Puffin Crossing |
|20| Program for Burglar Alaram using ESP32 |
|21| Program for DHT11 |
---------------------

|  **Program-1** | 
| :---- |
|Program to blink LED  |
|[Source Code](Programs/Blink.py)|

--------------------

| **Program-2** |
| :---- |
|Program to Get input from two switches and switch on corresponding LEDs.|
|[Source Code](Programs/PB-LED.py)|

------------------

|  **Program-3** |
| :---- |
|Program to Flash an LED at a given on time and off time cycle, where the two times are taken from a file. |
|[Source Code](Programs/file.py)|

-------------------

|  **Program-4** |
| :---- |
|Program to Switch on a relay at a given time using sleep function, where the relay’s contact terminals are connected to a load.|
|[Source Code](Programs/Relay.py)|

---------------------

|  **Program-5** |
| :---- |
|Program for Buzzer |
|[Source Code](Programs/buzzer.py)|

-----------------------

|  **Program-6** |
| :---- |
|Program for Thermistor  |
|[Source Code](Programs/Thermister.py)|

------------------------

|  **Program-7** |
| :---- |
|Program for Light Dependent Resistor(LDR) |
|[Source Code](Programs/ldr.py)|

------------------------

|  **Program-8** |
| :---- |
|Implement an intruder system that sends an alert to the given email|
|[Source Code](Programs/pir.py)|

-----------------------

|  **Program-9** |
| :---- |
|Control Relay Module with MicroPython Web Server|
|[Boot Code](Programs/boot.py)|
|[Main Code](Programs/main.py)|

-------------------------

|  **Program-10** |
| :---- |
|Get an alarm from a remote area if smoke is detected.|
|[Source Code](Programs/smoke.py)|

-------------------------------

<h3 align = "center">Don't forget to ⭐ this repo<h3>
  
  ---------------------------

