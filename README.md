# XMAGE: IMAGE MUTATION
Xmage is an open-source user interface for serveral GAN models based on PyTorch.

**New Features/Updates**
- June 3th, 2023: Add the UI code and ESRGAN model for restoration.

If this repo helps your research or work, please help me to ⭐ this repo. Thank you so much.

<p align="center">
  <img src="assets/web-index.jpg">
</p>

---

## Getting started
### Installation

- Let's clone this repo:
```bash
git clone https://github.com/lucaznguyen/xmage.git
cd xmage
```

- Create the virtual environment and activate it:
```bash
python -m venv venv
venv/Scripts/activate
```

- Install the required packages:
```bash
pip install -r requirements.txt
```

- Download the pretrained model `gen.pth`, `disc.pth` [here](https://drive.google.com/drive/folders/1zJ65Pb1cJ-JRousOqVO-lufJ86gNuFeM?usp=sharing) and put it into `esrgan/` folder.

### Run the Web UI

Simply run `python main.py` and open the host server address `http://127.0.0.1:5000` to enjoy the application.

<p align="center">
  <img src="assets/web-service.jpg">
</p>

### ESRGAN

This is a PyTorch implementation of the paper [ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks](https://arxiv.org/abs/1809.00219). This model is trained using the [Celebrity Face Image Dataset](https://www.kaggle.com/datasets/vishesh1412/celebrity-face-image-dataset) on Kaggle.

Let's train the model from scratch:
- Download the dataset and drop it into the folder `esrgan/data`.
- Set the value `LOAD_MODEL = False` in `esrgan/config.py` to train the model from scratch, otherwise it will load the previous model to continue training at the checkpoint.
- Set the value `try_model = False` in `esrgan/train.py` and run the code `python esrgan/train.py`.

Try restoring some images:
- This model works best with 500x500 pixel image.
- Create the folder `esrgan/test_images` and drop a few low-resolution images into it.
- Set the value `try_model = True` in `esrgan/train.py` and run the code `python esrgan/train.py`.

<p align="center">
  <img src="assets/web-enhance.jpg">
</p>

---

## Roadmap

- [x] Create the Web UI.
- [x] Add ESRGAN model to enhance images.
- [ ] Add GFPGAN model to restore old images.
- [ ] Add Text2Image model to create image using text prompt.
  - [x] Build Text2Image model using DCGAN.
  - [x] Collect the [Oxford Flower Dataset](https://www.robots.ox.ac.uk/~vgg/data/flowers/) and ready for tranining.
  - [ ] Train the model and save the pretrained one.
- [ ] Build STYLEGAN model to create image from serveral diffrent ones.

---

## License

This project is released under the [Apache 2.0 license](LICENSE).<br>

---

## Contact

If you have any questions, please send me a message through `thinhnguyenresearch@gmail.com`, `thinh.nth@vinuni.edu.vn`.

## References

> Wang, Xintao, et al. "Esrgan: Enhanced super-resolution generative adversarial networks." Proceedings of the European conference on computer vision (ECCV) workshops. 2018. <https://github.com/xinntao/ESRGAN> 

> Reed, Scott, et al. "Generative adversarial text to image synthesis." International conference on machine learning. PMLR, 2016. <https://github.com/reedscot/icml2016>

> Studio, Bootstrap. "Creating a Website with Bootstrap Studio (Tutorial)." Youtube, Aug 17 (2016): 1.
