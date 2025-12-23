# HOI4D 4D data pipeline (bug fixed)
Fixed numerous bugs in the original code provided by the https://github.com/leolyliu/HOI4D-Instructions.
## Data Organization

HOI4D is constructed by collected human-object interaction RGB-D videos and various annotations including object CAD models, action segmentation, 2D motion segmentation, 3D static scene panoptic segmentation, 4D dymanics scene panoptic segmentation, category-level object pose, and human hand pose.

run `orgnize_files.ipynb` to organize data as follow:

```
./ZY2021080000*/H*/C*/N*/S*/s*/T*/
|--align_rgb
   |--image.mp4
|--align_depth
   |--depth_video.avi
|--objpose
   |--*.json
|--action
   |--color.json
|--3Dseg
   |--raw_pc.pcd
   |--output.log
   |--label.pcd
|--2Dseg
   |--mask
```
- ZY2021080000* refers to the camera ID.
- H* refers to human ID.
- C* refers to object class.    
```
mapping = [
    '', 'ToyCar', 'Mug', 'Laptop', 'StorageFurniture', 'Bottle',
    'Safe', 'Bowl', 'Bucket', 'Scissors', '', 'Pliers', 'Kettle',
    'Knife', 'TrashCan', '', '', 'Lamp', 'Stapler', '', 'Chair'
]
```
- N* refers to object instance ID.
- S* refers to the room ID.
- s* refers to the room layout ID.
- T* refers to the task ID.

## Build the pipeline

### A. Decode the RGB and Depth

1. First you need to install [ffmpeg](https://ffmpeg.org/).
2. Then run ``` python utils/decode.py``` to generate RGB and depth images.

**The provided program must be executed; otherwise, the depth data will be corrupted.**

### B. reconstruct per frame 3D to get 4D

modify the `very_few_samples.txt` to control the scene to be used.

then follow the command

```
python prepare_4Dseg/prepare_4Dseg_dataset.py --data_dir /PATH/TO/HOI4D --output_dir /PATH/TO/HOI4D_4Dseg
```

**Each execution of the program will remove previously decoded RGBD data. If you need to keep it, please modify `utils/decode.py` accordingly.**

## Citation

Please cite HOI4D if it helps your research: 

```x
@inproceedings{liu2022hoi4d,
  title={HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction},
  author={Liu, Yunze and Liu, Yun and Jiang, Che and Lyu, Kangbo and Wan, Weikang and Shen, Hao and Liang, Boqiang and Fu, Zhoujie and Wang, He and Yi, Li},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={21013--21022},
  year={2022}
}
```

