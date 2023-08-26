# VITS: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech

## For Setup

#### Step 1 (Clone the git repo)

```sh

git clone https://github.com/newton2149/vits-tts.git

```

#### Step 2 (Install Required Dependencies) (Skip this test if you are using docker)
```sh
pip3 install -r requiremnts.txt
```

#### Step 3 (Build Monotonic Align) (Skip this test if you are using docker)
```sh
cd monotonic_align
mkdir monotonic_align
python setup.py build_ext --inplace

```

#### Step 4 (Download Model from Google Drive Link) (Skip this test if you are using docker)

[Google Drive Link](https://drive.google.com/drive/folders/1ksarh-cJf3F5eKJjLVWY0X1j1qsQqiS2?usp=sharing)


## For Inferencing Using the local Setup

### For VCTK Model

```sh
python3 vctk_inference.py --text "text completed" --device "cpu" --speaker_id 10 --noise_scale 0.669 --noise_scale_w 0.9 --length_scale 2 

```

### For LJ Model

```sh
python3 LJ_Inference.py --text "text completed" --device "cpu" --noise_scale 0.669 --noise_scale_w 0.9 --length_scale 2 

```


## Inferencing Using Docker

#### Step 1 

Install Docker

#### Step 2 (Docker Pull the Image)

```sh
docker pull newton2149/vits:v01

```
### For VCTK Model

```sh
 docker run -v $(pwd):/usr/src/vits_app newton2149/vits:latest python3 vctk_inference.py --text "text completed" --device "cpu" --speaker_id 10 --noise_scale 0.669 --noise_scale_w 0.9 --length_scale 2 

```

### For LJ Model

```sh
 docker run -v $(pwd):/usr/src/vits_app newton2149/vits:latest python3 LJ_Inference.py --text "text completed" --device "cpu" --noise_scale 0.669 --noise_scale_w 0.9 --length_scale 2 

```
