## SST IoT Development Board Experiments Using MicroPython

| **Python Installation Guide** |
| :---------- |
|[Click Here](Python-Installation.md)|

-----------------

| **Installation of upycraft IDE** |
| :------------ |
[Click Here](uPycraft-Installation.md)

-------------------


| **Flash/Upload MicroPython Firmware to ESP32** |
| :------------ |
[Click Here](Flash.md)

-------------------------

### About the Board
The **SST IoT Development Board** is a ESP-32 Module mounted on a custom PCB and integrated with different Sensors and Accuators, using which strong Embedded and IoT fundamentals are developed by deploying and implementing various projects involving cloud, ML and various other industry stacks.

--------------

### Specifications

- The ESP32 is dual core, this means it has 2 processors.
- It has Wi-Fi and bluetooth built-in.
- It runs 32 bit programs.
- The clock frequency can go up to 240MHz and it has a 512 kB RAM.
- This particular board has 30 pins, 15 in each row.
- It also has wide variety of peripherals available, like: capacitive touch, ADCs, DACs, UART, SPI, I2C and much more.
- It comes with built-in hall effect sensor and built-in temperature sensor.

-----------------

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
|1|Program to blink LED |
|2|Program to Get input from two switches and switch on corresponding LEDs.|
|3|Program to Flash an LED at a given on time and off time cycle, where the two times are taken from a file.|
|4|Program to Switch on a relay at a given time using sleep function, where the relay’s contact terminals are connected to a load.|
|5|Program for Buzzer |
|6|Program for Thermistor|
|7|Program for Light Dependent Resistor(LDR)|
|8|Program to monitor Temperature and Humidity using DHT11|
|9|Program to Handle Interruption|
|10|Program to control LED using Client/Server Architecture |
|11| Program to control Blulb using Relay and Client/Server Architecture|

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
|Program to monitor Temperature and Humidity using DHT11 |
|[Source Code](Programs/dht11.py)|

--------------------------

|  **Program-9** |
| :---- |
|Program to handle Interruption |
|[Source Code](Programs/pir.py)|

-----------------------

|  **Program-10** |
| :---- |
|Program to control LED using Client/Server Architecture  |
|[Source Code](Programs/main.py)|

-------------------------

|  **Program-11** |
| :---- |
|Program to control Blulb using Relay and Client/Server Architecture |
|[Source Code](Programs/relayControl.py)|



