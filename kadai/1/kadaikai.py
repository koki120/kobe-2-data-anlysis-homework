import pandas as pd
import numpy as np
from sklearn import linear_model

# 引数ddof=1とするとn-1で割る標準偏差が使われる. デフォルトはaxis=Noneで配列全体


def standardization(x: np.ndarray, axis=None, ddof=1) -> np.ndarray:
    x_mean = x.mean(axis=axis, keepdims=True)
    x_std = x.std(axis=axis, keepdims=True, ddof=ddof)
    result = (x - x_mean) / x_std
    return result


economicData = pd.read_csv(
    '1/県内総生産.csv', sep=',')
municipalityAndAreaData = pd.read_csv(
    '1/市町村数と面積.csv', sep=',')
populationData = pd.read_csv(
    '1/年齢区分別人口.csv', sep=',')
merged_data = pd.merge(municipalityAndAreaData, populationData, on='都道府県')

# 回帰モデルの呼び出し
clf = linear_model.LinearRegression()

# 説明変数
x = merged_data[['市', '町', '村', '総面積',
                 '0歳から14歳', '15歳から64歳', '65歳以上']].values


# 目的変数
y = economicData['名目県内総生産'].values


# 予測モデルを作成（重回帰）
clf.fit(x, y)

# 回帰係数と切片の抽出
a = clf.coef_
b = clf.intercept_
r_squared = clf.score(x, y)
n = x.shape[0]
k = x.shape[1]
adjusted_r_squared = r_squared*(n-1)/(n-1-k) - k/(n-1-k)
# 回帰係数
print("回帰係数:", a)
print("切片:", b)
print("決定係数:", r_squared)
print("自由度調整済み決定係数:", adjusted_r_squared)
