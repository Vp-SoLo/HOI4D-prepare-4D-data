import os
import subprocess
import sys
import logging

import os

def clean_dir_keep_videos(rgb_dir, depth_dir):

    keep_map = {
        rgb_dir: {"image.mp4"},
        depth_dir: {"depth_video.avi"},
    }

    for dir_path, keep_files in keep_map.items():
        if not os.path.isdir(dir_path):
            print("SKIP (not dir):", dir_path)
            continue

        for name in os.listdir(dir_path):
            full_path = os.path.join(dir_path, name)

            # 只处理普通文件
            if not os.path.isfile(full_path):
                continue

            if name in keep_files:
                continue

            print("REMOVE:", full_path)
            os.remove(full_path)

def decode_video(root):

    with open('./very_few_samples.txt', 'r') as f:
        rgb_list = [os.path.join(root, i.strip(),'align_rgb') for i in f.readlines()]

    for rgb in rgb_list:
        depth = rgb.replace('align_rgb','align_depth')
        rgb_video = os.path.join(rgb, "image.mp4")
        depth_video = os.path.join(depth, "depth_video.avi")

        # comment this to keep data
        clean_dir_keep_videos(rgb, depth)

        cmd =  """ ffmpeg -i {} -f image2 -start_number 0 -vf fps=fps=15 -qscale:v 2 {}/%05d.{} -loglevel quiet """.format(rgb_video, rgb, "jpg")

        print(cmd)
        p = subprocess.Popen(cmd, shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if err:
            logging.info(err.decode())

        cmd = """ ffmpeg -i {} -f image2 -start_number 0 -vf fps=fps=15 -qscale:v 2 {}/%05d.{} -loglevel quiet """.format(depth_video, depth, "png")
        print(cmd)

        p = subprocess.Popen(cmd, shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if err:
            logging.info(err.decode())

if __name__ == '__main__':
    decode_video('/mnt/hdd/yangqitong/datasets/HOI4D/')
