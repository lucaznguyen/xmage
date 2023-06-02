# XMAGE: MUTATING IMAGES
Xmage is an open-source user interface for serveral GAN models based on PyTorch.

**New Features/Updates**
- June 3th, 2023: Add the UI code and ESRGAN model for restoration.

---

If this repo helps your research or work, please help to ⭐ this repo. Thank you so much.

## Getting started
### Installation

Let's clone this repo:
```bash
git clone https://gitlab.com/lucaznguyen/xmage.git
cd xmage
```

Create the virtual environment and activate it:
```bash
python -m venv
venv/Script/activate
```

Install the requirement package:
```bash
pip install -r requirements.txt
```

### Run the Web UI

Simply run `python main.py` and open the host server address `http://127.0.0.1:5000` to enjoy the application.

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


## License and Acknowledgement

This project is released under the [Apache 2.0 license](LICENSE).<br>

## Contact

If you have any questions, please email `lucaznguyenofficial@gmail.com`, `21c29018@student.hcmus.edu.vn`.
