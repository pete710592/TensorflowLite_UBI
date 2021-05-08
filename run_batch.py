import os
from tqdm import tqdm
import glob

class Detection():
    def image_batch(self):
        models = glob.glob('TFLite_model/08*')
        images = glob.glob('images/Car_02_04m.jpg')
        for image in tqdm(images):
            for model in models:
                cmd = f'python3 TFLite_detection_image.py --modeldir="{model}" --image={image} --display_label=2'
                os.system(cmd)
    
    def video_batch(self):
        models = glob.glob('TFLite_model/08*')
        videos = glob.glob('videos/Cityscape_01*.mp4')
        for video in tqdm(videos):
            for model in models:
                cmd = f'python3 TFLite_detection_video.py --modeldir="{model}" --video={video} --display_label=2'
                os.system(cmd)

if __name__ == '__main__':
    detection = Detection()
    detection.image_batch()
    # detection.video_batch()