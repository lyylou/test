import tensorflow as tf
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
import numpy as np
import sklearn 
import os
import sys
from tensorflow import keras
print(sys.version_info)
for model in tf,keras,mpl,np,pd,sklearn:
    print(model.__name__,model.__version__)
