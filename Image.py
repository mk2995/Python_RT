"""
Image.py
Creates an image using a PPM file
Author Matthew Klein
"""
import Vectors
import math

WIDTH = 320
HEIGHT = 200


# Creates a blank 2-D array of pixels that every function can manipulate
def image(width, height):
    # Global pixel array each function can access
    global PIXELS
    PIXELS = [[None for _ in range(width)] for _ in range(height)]
    return PIXELS


# Allows the user to set the color of individual pixels
def set_pixels(x, y, color):
    PIXELS[y][x] = color


# Helper function ensuring values stay in range between 0 - 255
def byter(num):
    return round(max(min(num * 255, 255), 0))


# Determines how many times a ray passes through a sphere and calculates distance accordingly
def ray_sphere_intersection(ray, sphere):
    a = 1
    b = 2 * Vectors.dot_product(ray[1], Vectors.subtraction(ray[0], sphere[0]))
    c = Vectors.dot_product(Vectors.subtraction(ray[0], sphere[0]),
                            Vectors.subtraction(ray[0], sphere[0])) - (sphere[1] ** 2)
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant >= 0:
        dist = (-b - math.sqrt(discriminant)) / (2 * a)
        if dist > 0:
            return dist


# An instance of a 3-D ray
def ray(origin, direction):
    return [origin, Vectors.normalize(direction)]


# An instance of a 3-D position hit by a ray
def hit_pos(origin, direction, dist):
    return Vectors.addition(origin, Vectors.scalar(dist, direction))


# An instance of a sphere that checks if a ray intersects with it
def sphere(center, radius, color):
    return [center, radius, color]


# The scene contains the information necessary to render an image
def scene(camera, objects, width, height):
    return [camera, objects, width, height]


# Finds the nearest object relative to the ray()
def find_nearest(ray, scene):
    dist_min = None
    obj_hit = None
    for i in scene[1]:
        dist = ray_sphere_intersection(ray, i)
        if dist is not None and (obj_hit is None or dist < dist_min):
            dist_min = dist
            obj_hit = i
    return dist_min, obj_hit


# Determines the color of a hit object
def color_at(obj, position, scene):
    return obj[2]


# Locates the closest object hit by the scene
def ray_trace(ray, scene):
    color = [0, 0, 0]
    dist_hit, obj_hit = find_nearest(ray, scene)
    if obj_hit is None:
        return color
    hit = hit_pos(ray[0], ray[1], dist_hit)
    color = Vectors.addition(color, color_at(obj_hit, hit, scene))
    return color


# Scene uses given information to generate 3-D objects into a 2-D image
def render_engine(scene):
    aspect_ratio = float(scene[2]) / scene[3]
    x_max = -1.0
    x_min = 1.0
    x_step = (x_min - x_max) / (scene[2] - 1)

    y_max = -1.0 / aspect_ratio
    y_min = 1.0 / aspect_ratio
    y_step = (y_min - y_max) / (scene[3] - 1)

    image(scene[2], scene[3])

    for j in range(scene[3]):
        y = y_max + j*y_step
        for i in range(scene[2]):
            x = x_max + i*x_step
            screen_ray = ray(scene[0], Vectors.subtraction([x, y, 0], scene[0]))
            set_pixels(i, j, ray_trace(screen_ray, scene))


# Writes pixel information to a ppm file
def file_writer(file_name):
    with open(file_name, 'w') as img_file:
        img_file.write("P3 " + str(WIDTH) + " " + str(HEIGHT) + "\n" + str(255) + "\n")
        for row in PIXELS:
            for color in row:
                img_file.write(str(byter(color[0])) + " " + str(byter(color[1])) + " " + str(byter(color[2])) + " ")
            img_file.write("\n")


def main():
    red = [1, 0, 0]
    camera = [0, 0, -1]
    objects = [sphere([0, 0, 0], 0.5, red)]
    sc = scene(camera, objects, WIDTH, HEIGHT)
    render_engine(sc)
    file_writer("RayTracing/test.ppm")


main()