## SP24-IXD-256-ClaireLi Code Repository

# #Assignment #1.

#### To enhance students' time management during their morning makeup routine, I devised a system involving two pieces of copper tape affixed to the cover of a mirror. These pieces are wired to the M5 Atom board. When the two pieces of copper tape pieces make contact, the electrical circuit closes, signaling the input as "on"; otherwise, it remains "off". Once the digital input is "on", the Atom board initiates a process of drawing one pixel per second, gradually filling the display with nine pixels, representing nine seconds. Upon completion of the nine-second countdown, the display triggers visibility for a label indicating that time is up, prompting the user to finish up and prepare for school promptly to avoid tardiness.

[Micro Python Code](Assignment%20%231%20/code)
![state diagram](https://github.com/wli14/SP24_IXD256_ClaireLi/assets/158603687/a13db355-3ec4-4e27-8030-f76eedb8df86)

# #Assignment #2.

#### To enhance children's enthusiasm for learning about color saturation and value, I've devised a wearable bracelet that integrates sensors such as the Inertial Measurement Unit (IMU) and potentiometer (M5 ANGLE unit). Through this innovation, I translate the analog input values captured from the two sensors into computer graphics output, thereby providing an immersive, intuitive, and interactive experience. In the code, I established a mapping between color saturation levels ranging from 0 to 255 and the potentiometer values ranging from 0 to 4095. Additionally, I monitored X and Y tilt as well as X and Y motion using the IMU accelerometer. These values were then mapped from five distinct states to five corresponding color patterns on the computer output. As for the physical prototype, I utilized tie braids as a fabrication method and specifically used neoprene fabric, which is a rubber composition that offers waterproof properties, stretchiness, and excellent heat retention. This material is not only chemically stable but also remarkably flexible across a broad temperature spectrum. Its characteristics make it particularly suitable for children's use, ensuring durability and comfort during learning activities.

[Hardware Code IMU+ADC](https://github.com/wli14/SP24_IXD256_ClaireLi/blob/main/wk5%20-%20hw/hardware(IMU%20%2B%20ADC))
[Software Code File](https://github.com/wli14/SP24_IXD256_ClaireLi/tree/main/wk5%20-%20hw/webserial_pyscript_p5)
![State Diagram](https://github.com/wli14/SP24_IXD256_ClaireLi/assets/158603687/82dbd9b9-5dd9-4f7a-beaa-88e01aa7f025)
![Prototype](https://github.com/wli14/SP24_IXD256_ClaireLi/assets/158603687/46276b63-68be-4f5d-877c-69d9b3c59bd0)


# #Assignment #3.

#### The concept is to demonstrate a clock that operates based on the amount of light throughout the day, utilizing a Photoresistor (M5 LIGHT unit) as an input to control a 180-degree servo as an output.

[Hardware Code PHOTORESISTOR+SERVO](https://github.com/wli14/SP24_IXD256_ClaireLi/blob/main/w8%20-%20hw/py)
![Original Concept Sketch](https://github.com/wli14/SP24_IXD256_ClaireLi/assets/158603687/f5385510-55b0-431e-98d4-b5ba70aa9964)
![State Image](https://github.com/wli14/SP24_IXD256_ClaireLi/assets/158603687/623b3273-f84a-4338-8ee0-a17dbb10255b)

![code 01](https://github.com/wli14/SP24_IXD256_ClaireLi/assets/158603687/200ec2b2-8ca8-4602-b0d5-1f3fbb68f6af)
#### Used function with five parameters: in_val (the input value to be mapped), in_min and in_max (the minimum and maximum values of the input range), out_min and out_max (the minimum and maximum values of the output range) to map the input value from the input range to the output range using linear interpolation.  Constrained the mapped value to be within the output range.
![code 2](https://github.com/wli14/SP24_IXD256_ClaireLi/assets/158603687/4d0096bf-364e-4e19-bde0-3d6cfcd04a44)
#### Used (light_sensor.read()) to read a value from light sensor, assuming it returns a value in the range of 0 to 4095 (a 12-bit ADC value), then maps this value to a range between 60 and 170 using the map_value function.Compare the current servo_val with the servo_val_final . If the current servo_val is less than servo_val_final, it increments servo_val by 1. If it's greater, it decrements servo_val by 1. Finally, the servo moves to the new position represented by servo_val.
