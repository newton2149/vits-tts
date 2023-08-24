# VITS: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech

## For Setup

#### Step 1 (Install Required Dependencies)
```sh
pip3 install -r requiremnts.txt
```

#### Step 2 (Build Monotonic Align)
```sh
cd monotonic_align
mkdir monotonic_align
python setup.py build_ext --inplace

```

#### Step 3 (Download Model from Google Drive Link)

[Google Drive Link](https://drive.google.com/drive/folders/1ksarh-cJf3F5eKJjLVWY0X1j1qsQqiS2?usp=sharing)

### For VCTK Model

```sh
python3 vctk_inference.py --text "text completed" --device "cpu" --speaker_id 10 --noise_scale 0.669 --noise_scale_w 0.9 --length_scale 2 

```

### For LJ Model

```sh
python3 LJ_Inference.py --text "text completed" --device "cpu" --noise_scale 0.669 --noise_scale_w 0.9 --length_scale 2 

```

