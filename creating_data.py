import cv2, os, time

IMAGES_PATH = 'dataset'
try:
    os.mkdir(IMAGES_PATH)
except OSError:
    pass
labels = [ 'nice to meet you', 'hello', 'thanks', 'yes', 'no',
           'iloveyou', 'please', 'sorry', 'you\'re welcome',]
NUMBER_IMGS = 15

for label in labels:
    try:
        os.mkdir(os.path.join(IMAGES_PATH, label))
    except OSError as error:
        pass
    capture = cv2.VideoCapture(0)
    print(f'Collecting images for {label}')
    time.sleep(15)
    for image_num in range(NUMBER_IMGS):
        ret, frame = capture.read()
        image_name = os.path.join(IMAGES_PATH, label, f'{label}_{image_num}.jpg')
        cv2.imwrite(image_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(3)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()