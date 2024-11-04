# 라이브러리 임포트
import os
import pandas as pd
import dask.dataframe as dd
import time

filepath = 'G:\\내 드라이브\\DataSet\\_파킷 파일\\서울특별시 공공자전거 대여이력 정보\\'

from dask.distributed import Client
start_time = time.time()
client = Client(n_workers=4)
df = dd.read_parquet(filepath + '서울특별시 공공자전거 대여이력 정보_20~24.parquet').compute()
print("read_parquet time :", time.time() - start_time)

