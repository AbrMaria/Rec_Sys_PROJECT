

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from tqdm import tqdm_n

# датасет с отзывами по англоязычным курсам
reviews_eng_courses = pd.read_csv(
    '‎../iCloud Drive/Desktop/Нетология/Рекоменд системы/Rec_Sys_PROJECT/reviews_eng_courses.csv')
# reviews_eng_courses = pd.read_csv('https://github.com/AbrMaria/Rec_Sys_PROJECT/blob/master/reviews_eng_courses.csv')
reviews_eng_courses.head()
