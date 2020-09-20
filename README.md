# Python_RT
This program utilizes Python's mutable list datatype as the foundation to render image files at compile time through Ray-tracing.

Run the file Image.py to create an image file (.ppm). 
  - To change the resolution of the image, edit the WIDTH and HIGHT constants wtithin Image.py
  - To change the object within the image, edit main() with your desired object feild then give it a shape that has a specified position, size,
    and color (e.g. objects = [sphere([0, 0, 0], 0.5, red)]). 
  - Colors are generated using vectors that contain RGB values that range from 0-1 for each color value.
