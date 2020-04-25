# Single Shot MultiBox Detector Implementation in Pytorch

This repo implements [SSD (Single Shot MultiBox Detector)](https://arxiv.org/abs/1512.02325).  
The implementation is heavily influenced by the projects [ssd.pytorch](https://github.com/amdegroot/ssd.pytorch) and [Detectron](https://github.com/facebookresearch/Detectron).
The design goal is modularity and extensibility.

Currently, it has MobileNetV1, MobileNetV2, and VGG based SSD/SSD-Lite implementations. 

It also has out-of-box support for retraining on Google Open Images dataset.

![Example of Mobile SSD](readme_ssd_example.jpg)

## Dependencies
1. Python 3.6+
2. OpenCV
3. Pytorch 1.0 or Pytorch 0.4+
4. Pandas

## Pretrained Models

### Mobilenet V1 SSD

URL: https://storage.googleapis.com/models-hao/mobilenet-v1-ssd-mp-0_675.pth

```
Average Precision Per-class:
aeroplane: 0.6742489426027927
bicycle: 0.7913672875238116
bird: 0.612096015101108
boat: 0.5616407126931772
bottle: 0.3471259064860268
bus: 0.7742298893362103
car: 0.7284171192326804
cat: 0.8360675520354323
chair: 0.5142295855384792
cow: 0.6244090341627014
diningtable: 0.7060035669312754
dog: 0.7849252606216821
horse: 0.8202146617282785
motorbike: 0.793578272243471
person: 0.7042670984734087
pottedplant: 0.40257147509774405
sheep: 0.6071252282334352
sofa: 0.7549120254763918
train: 0.8270992920206008
tvmonitor: 0.6459903029666852

Average Precision Across All Classes:0.6755
```

### MobileNetV2 SSD-Lite

URL: https://storage.googleapis.com/models-hao/mb2-ssd-lite-mp-0_686.pth

```
Average Precision Per-class:
aeroplane: 0.6973327307871002
bicycle: 0.7823755921687233
bird: 0.6342429230125619
boat: 0.5478160937380846
bottle: 0.3564069147093762
bus: 0.7882037885117419
car: 0.7444122242934775
cat: 0.8198865557991936
chair: 0.5378973422880109
cow: 0.6186076149254742
diningtable: 0.7369559500950861
dog: 0.7848265495754562
horse: 0.8222948787839229
motorbike: 0.8057808854619948
person: 0.7176976451996411
pottedplant: 0.42802932547480066
sheep: 0.6259124005994047
sofa: 0.7840368059271103
train: 0.8331588002612781
tvmonitor: 0.6555051795079904
Average Precision Across All Classes:0.6860690100560214
```

The code to re-produce the model:

```bash
$ wget -P models https://storage.googleapis.com/models-hao/mb2-imagenet-71_8.pth
```

### VGG SSD

URL: https://storage.googleapis.com/models-hao/vgg16-ssd-mp-0_7726.pth


```
Average Precision Per-class:
aeroplane: 0.7957406334737802i
bicycle: 0.8305351156180996
bird: 0.7570969203281721
boat: 0.7043869846367731
bottle: 0.5151666571756393
bus: 0.8375121237865507
car: 0.8581508869699901
cat: 0.8696185705648963
chair: 0.6165431194526735
cow: 0.8066422244852381
diningtable: 0.7629391213959706
dog: 0.8444541531856452
horse: 0.8691922094815812
motorbike: 0.8496564646906418
person: 0.793785185549561
pottedplant: 0.5233462463152305
sheep: 0.7786762429478917
sofa: 0.8024887701948746
train: 0.8713861172265407
tvmonitor: 0.7650514925384194
Average Precision Across All Classes:0.7726184620009084
```

The code to re-produce the model:

```bash
$ wget -P models https://s3.amazonaws.com/amdegroot-models/vgg16_reducedfc.pth
```

## Training

```bash
$ wget -P models https://storage.googleapis.com/models-hao/mobilenet_v1_with_relu_69_5.pth  
or  
$ python3 download-model.py
```
```bash
$ python3 download-dataset.py
$ python3 train_ssd.py --dataset_type track_and_trail --datasets dataset --validation_dataset dataset --net mb1-ssd --base_net models/mobilenet_v1_with_relu_69_5.pth --lr 0.01 --validation_epochs 10 --num_epochs 800

```


The dataset path is the parent directory of the folders: Annotations, JPEGImages.  
You can use multiple datasets to train.


## Evaluation

```bash
python3 eval_ssd.py --net mb1-ssd  --dataset dataset --trained_model models/Epoch-740-Loss-0.8609.pth --label_file models/track_and_trail.txt --dataset_type track_and_trail 
```
