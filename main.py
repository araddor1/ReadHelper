from VideoCapture import *
import DataPreProccess.MPIIDataLoader as MPIIDataLoader
import DataPreProccess.trainNet as trainNet
import h5py
import numpy as np

dataset_path = 'RES/MPIIGaze.h5'

def __main__():
    print("hello world!")
    start_camera()
    # trainNet.train_and_validate_aux(1)




if __name__ == "__main__":
    __main__()
