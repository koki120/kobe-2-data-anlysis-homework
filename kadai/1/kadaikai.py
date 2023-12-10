from math import sqrt
import pandas as pd
from sklearn import linear_model
from sklearn.decomposition import PCA

economicData = pd.read_csv(
    '1/県内総生産.csv', sep=',')
municipalityAndAreaData = pd.read_csv(
    '1/市町村数と面積.csv', sep=',')
populationData = pd.read_csv(
    '1/年齢区分別人口.csv', sep=',')
merged_data = pd.merge(municipalityAndAreaData, populationData, on='都道府県')


# 回帰分析

# 回帰モデルの呼び出し
clf = linear_model.LinearRegression()

# 説明変数
x = merged_data[['市', '町', '村', '総面積',
                 '0歳から14歳', '15歳から64歳', '65歳以上']].values


# 目的変数
y = economicData['名目県内総生産'].values


# 予測モデルを作成（重回帰）
clf.fit(x, y)


# 結果を表示
a = clf.coef_
b = clf.intercept_
r_squared = clf.score(x, y)
n = x.shape[0]
k = x.shape[1]
adjusted_r_squared = r_squared*(n-1)/(n-1-k) - k/(n-1-k)
print("回帰係数:", a)
print("切片:", b)
# 定義が[残差変動の平方和/((全変動の平方和*回帰変動の平方和)の2乗根)]なので負にならない
print("重相関係数:", sqrt(r_squared))
print("決定係数:", r_squared)
print("自由度調整済み決定係数:", adjusted_r_squared)


# 主成分分析

all_merged_data = pd.merge(economicData, merged_data, on='都道府県')
df = all_merged_data[['都道府県', '名目県内総生産', '市', '町',
                      '村', '総面積', '0歳から14歳', '15歳から64歳', '65歳以上']]
# 標準化
dfs = df.iloc[:, 1:].apply(lambda x: (x-x.mean())/x.std(), axis=0)

# 主成分分析の実行
pca = PCA()
pca.fit(dfs)

# データを主成分空間に写像 & 都道府県のラベルを貼る
feature = pd.DataFrame(pca.transform(dfs), index=df.values[:, 0])

# 寄与率
explained_variance_ratio = pd.DataFrame(pca.explained_variance_ratio_, index=[
    "PC{}".format(x + 1) for x in range(len(dfs.columns))])

print(explained_variance_ratio)

# PCA の固有ベクトル
eigenvector = pd.DataFrame(pca.components_, columns=df.columns[1:], index=[
    "PC{}".format(x + 1) for x in range(len(dfs.columns))])

print(eigenvector)
