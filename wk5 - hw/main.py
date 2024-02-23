import js as p5
from js import document

data_string = None
data_list = None
sensor_val = None
state = None

def setup():
    p5.createCanvas(300, 300)

def draw():
    p5.background(255)
    global data_string, data_list
    global sensor_val, state

    # assign content of "data" div on index.html page to variable:
    data_string = document.getElementById("data").innerText
    # split data_string by comma, making a list:
    data_list = data_string.split(',')

    # assign 1st item of data_list to sensor_val:
    sensor_val = int(data_list[0])
    # assign 2nd item of data_list to state:
    state = int(data_list[1])

    p5.noStroke()  # disable stroke

    # draw 20 columns and 20 rows of the same circle, changing saturation with sensor data:
    p5.colorMode(p5.HSB)  # Switch to HSB color mode
    for i in range(20):
        for j in range(20):
            # Calculate position for each circle
            x = i * 20 + 10  # Starting position + (column index * distance between circles)
            y = j * 20 + 10  # Starting position + (row index * distance between circles)


            if (state == 0):
                # Calculate saturation based on sensor value
                saturation = p5.map(sensor_val, 0, 255, 0, 68)

                # Check if the current circle is in the 11th or 12th column
                if i == 10 or i == 11:
                    # Set the color to red with hue 9, saturation 69, and brightness 72
                    p5.fill(198, saturation, 50)
                else:
                    # Set the color to brown with hue 27, saturation 68, and brightness 58
                    p5.fill(360, saturation, 50)
                
                p5.ellipse(x, y, 20, 20)  # Use a fixed size for the circle
            elif (state == 1):
                # Calculate saturation based on sensor value
                saturation = p5.map(sensor_val, 0, 255, 0, 68)

                # Check if the current circle is in the 11th or 12th column
                if i == 10 or i == 11:
    
                    p5.fill(9, saturation, 59)
                else:
                
                    p5.fill(27, saturation, 58)
                
                p5.ellipse(x, y, 20, 20)  # Use a fixed size for the circle
