import cv2
import os

output_directory = r"E:\python\facenet\Facenet_Tensorflow-main\Facenet_Tensorflow-main\train_img\preetha"
frame_count = 25

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Count the number of existing frames in the directory
existing_frames = len(os.listdir(output_directory))

video = cv2.VideoCapture(0)  # Use index 0 for the default webcam

count = existing_frames + 1  # Start counting from the next frame after existing frames

while count <= existing_frames + frame_count:
    success, frame = video.read()
    name = os.path.join(output_directory, f"frame_{count}.jpg")

    if success:
        cv2.imwrite(name, frame)
        print(f"Frame {count} Extracted Successfully")
        count += 1
    else:
        break

video.release()
