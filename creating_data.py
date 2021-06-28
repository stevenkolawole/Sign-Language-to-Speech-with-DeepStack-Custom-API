import cv2, os, time, uuid

IMAGES_PATH = 'dataset'
try:
    os.mkdir(IMAGES_PATH)
except OSError:
    pass
labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
NUMBER_IMGS = 3

for label in labels:
    try:
        os.mkdir(os.path.join(IMAGES_PATH, label))
    except OSError as error:
        pass
    capture = cv2.VideoCapture(0)
    print(f'Collecting images for {label}')
    time.sleep(5)
    for image_num in range(NUMBER_IMGS):
        ret, frame = capture.read()
        image_name = os.path.join(IMAGES_PATH, label, f'{label}_{uuid.uuid1()}.jpg')
        cv2.imwrite(image_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(4)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()