from PIL import Image, ImageDraw

# Load the image you want to manipulate
image = Image.open("E:\Projects\Image manupulator\image.jpg")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define the coordinates for the different parts of the face
face_coords = (100, 100, 500, 500)
nose_coords = (250, 250, 350, 350)
mouth_coords = (200, 400, 400, 500)
left_eye_coords = (150, 200, 250, 300)
right_eye_coords = (350, 200, 450, 300)
left_ear_coords = (75, 225, 125, 375)
right_ear_coords = (475, 225, 525, 375)

# Define the colors for the different blocks
face_color = (255, 0, 0) # red
nose_color = (0, 255, 0) # green
mouth_color = (0, 0, 255) # blue
eye_color = (255, 255, 0) # yellow
ear_color = (0, 255, 255) # cyan

# Draw the blocks on the image using the defined coordinates and colors
draw.rectangle(face_coords, fill=face_color)
draw.rectangle(nose_coords, fill=nose_color)
draw.rectangle(mouth_coords, fill=mouth_color)
draw.rectangle(left_eye_coords, fill=eye_color)
draw.rectangle(right_eye_coords, fill=eye_color)
draw.rectangle(left_ear_coords, fill=ear_color)
draw.rectangle(right_ear_coords, fill=ear_color)

# Save the manipulated image
image.save("E:\Projects\Image manupulator\image.jpg")