import os
from tqdm import tqdm
import glob

class Detection():
    def image_batch(self):
        models = glob.glob('TFLite_model/08*')
        images = glob.glob('images/C*.jpg')
        for image in tqdm(images):
            for model in models:
                cmd = 'python3 TFLite_detection_image.py --modeldir="{}" --image={}'.format(model, image)
                os.system(cmd)
    
    def video_batch(self):
        models = glob.glob('TFLite_model/01*')
        videos = glob.glob('videos/09*.mp4')
        for video in tqdm(videos):
            for model in models:
                cmd = 'python3 TFLite_detection_video.py --modeldir="{}" --video={}'.format(model, video)
                os.system(cmd)

if __name__ == '__main__':
    detection = Detection()
    detection.image_batch()