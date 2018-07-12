import face_recognition
import cv2
import glob, os

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Initialize some variables
students_id = []
train_data = []
process_this_frame = True

DATA_PATH = "../data"

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)
url = "http://192.168.25.4:8080/shot.jpg?rnd=282868"

def check_camera(video_capture):
  return video_capture.read() != None

def add_student_to_train(image_path, student_id):
  print ('Loading image: ' + image_path)
  image = face_recognition.load_image_file(image_path)

  # Return the 128-dimension face encoding for each face in the image.
  fc_encodings = face_recognition.face_encodings(image)

  # If has at least one face, add it to train_data and label to students_id
  if len(fc_encodings) > 0:
    train_data.append(fc_encodings[0])
    students_id.append(student_id)

def write_file(file_path, list):
  file = open(file_path, "w")
  for element in list:
    file.write(element)
  file.close

  def read_file(file_path):
      file = open(file_path, "r")
      print (file)
      file.close()

def build_train():
  if check_camera(video_capture):
    for image_path in glob.glob(DATA_PATH + '/**/*.jpg'):
      student_id = os.path.dirname(image_path).split('/')[-1]
      add_student_to_train(image_path, student_id)

def recognize_image(frame, process_this_frame):
  # Resize frame of video to 1/4 size for faster face recognition processing
  small_frame = cv2.resize(frame, (0, 0), fx = 0.25, fy = 0.25)

  # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
  rgb_small_frame = small_frame[:, :, ::-1]

  # Only process every other frame of video to save time
  if process_this_frame:
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
      # See if the face is a match for the known face(s) in train data
      match = face_recognition.compare_faces(train_data, face_encoding, tolerance = 0.6)
      name = "Unknown"
      names = []

      for i in range(len(match)):
        if match[i]:
          name = students_id[i]

      names.append(name)

      process_this_frame = not process_this_frame

      # Display the results
      draw_rectangle(face_locations, names)


def draw_rectangle(face_locations, names):
  for (top, right, bottom, left), name in zip(face_locations, names):
    # Scale back up face locations since the frame we detected in was scaled to 1/4 size
    top *= 4
    right *= 4
    bottom *= 4
    left *= 4

    # Draw a box around the face
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Draw a label with a name below the face
    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 3)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

build_train()

while True:
    # Grab a single frame of video

    video_capture = cv2.VideoCapture(url)
    ret, frame = video_capture.read()

    if(check_camera(video_capture)):
        recognize_image(frame, process_this_frame)
    else:
        print 'An error occurred in frame. Please check the camera'
        break

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
