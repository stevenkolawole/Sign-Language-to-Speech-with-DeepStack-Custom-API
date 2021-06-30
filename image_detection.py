import argparse
import pyttsx3
from deepstack_sdk import Detection, ServerConfig


def predict_sign(image, port):
	"""
	Function to return the label, and coordinates of the bbox,
	while saving the new image (image with bbox) 
	and audiofile to directory.

	params
		image		name of the file
		port 		deepstack's server port, default is 88
	
	returns 
		image_new 	new image with sign's bbox
		image_audio	audio of the sign, converted by TTS synthesizer
	"""
	text_engine = pyttsx3.init()
	config = ServerConfig(f"http://localhost:{port}")
	detector = Detection(config=config, name="sign")

	name_stripped = image.rsplit('.', 1)[0]\
						 .replace("'", "_")\
						 .replace(" ", "_")

	detections = detector.detectObject(
		image=image,
		output=name_stripped + "_new.jpg")

	for detection in detections:
		print("Name: {}".format(detection.label))
		print("Confidence: {}".format(detection.confidence))
		print("x_min: {}".format(detection.x_min))
		print("x_max: {}".format(detection.x_max))
		print("y_min: {}".format(detection.y_min))
		print("y_max: {}".format(detection.y_max))

	if detection.label:
		text = detection.label
		audioname = name_stripped + "_audio.mp3" 
		text_engine.save_to_file(text, audioname)
		text_engine.runAndWait()


if __name__ == '__main__':
	# construct the argument parser and parse the arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("image_filename", 
						type=str,
						help="name of image to run inference on")
	parser.add_argument("--deepstack-port", 
						type=int,
						default=88,
						help="port on which the deepstack server's docker image is running")
	args = vars(parser.parse_args())

	image = args['image_filename']
	port = args['deepstack_port']
	predict_sign(image, port)