import pandas as pd
import numpy as np
import subprocess
import dask.dataframe as dd
import os
from tqdm import tqdm


def file_len(fname):
    "Function that calculates the number of rows in a dataset"
    p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])+1
