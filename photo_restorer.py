from model import Generator
from torchvision.utils import save_image

import torch
from torch import optim
import cv2

import albumentations as A
from albumentations.pytorch import ToTensorV2

test_transform = A.Compose(
    [
        A.Normalize(mean=[0, 0, 0], std=[1, 1, 1]),
        ToTensorV2(),
    ]
)

def load_checkpoint(checkpoint_file, model, optimizer, lr):
    print("=> Loading checkpoint")
    checkpoint = torch.load(checkpoint_file, map_location="cpu")
    # model.load_state_dict(checkpoint)
    model.load_state_dict(checkpoint["state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer"])
    
    for param_group in optimizer.param_groups:
        param_group["lr"] = lr

def predict_image(filename):
    gen = Generator(in_channels=3).to("cpu")
    opt_gen = optim.Adam(gen.parameters(), lr=1e-4, betas=(0.0, 0.9))
    load_checkpoint(
        "esrgan/gen.pth",
        gen,
        opt_gen,
        1e-4,
    )
    image = cv2.imread("static/images/" + filename)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    with torch.no_grad():
        upscaled_img = gen(
            test_transform(image=image)["image"].unsqueeze(0).to("cpu")
        )
    save_image(upscaled_img, "static/restored/" + filename)
    return "static/restored/" + filename