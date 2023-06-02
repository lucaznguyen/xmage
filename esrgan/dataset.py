import torch
from tqdm import tqdm
import time
import torch.nn
import os
from torch.utils.data import Dataset, DataLoader
import numpy as np
import config
from PIL import Image
import cv2
import glob


class MyImageFolder(Dataset):
    def __init__(self, root_dir):
        super(MyImageFolder, self).__init__()
        self.data = glob.glob(root_dir + "*")
        self.root_dir = root_dir
        self.class_names = os.listdir(root_dir)

        # img_dir = glob.glob(root_dir + "*")
        # print(img_dir[0])

        # for index, name in enumerate(self.class_names):
        # for index, files in enumerate(img_dir):
            # files = os.listdir(os.path.join(root_dir, name))
            # self.data.append([files, index * len(files)])
        # print("self.data", self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        # img_file, label = self.data[index][0], self.data[index][1]
        # root_and_dir = os.path.join(self.root_dir, self.class_names[label])
        image = cv2.imread(self.data[index])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        both_transform = config.both_transforms(image=image)["image"]
        low_res = config.lowres_transform(image=both_transform)["image"]
        high_res = config.highres_transform(image=both_transform)["image"]
        return low_res, high_res


def test():
    dataset = MyImageFolder(root_dir="data/")
    loader = DataLoader(dataset, batch_size=8)

    for low_res, high_res in loader:
        print(low_res.shape)
        print(high_res.shape)


if __name__ == "__main__":
    test()