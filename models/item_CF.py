#! /usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

# 计算 user_item_df, 初始化 item_item_df 矩阵


def user_item_table(rating_csv_path,):

    train_rating_raw = pd.read_csv(rating_csv_path)
    user_list = train_rating_raw['userId'].drop_duplicates().tolist()
    movie_list = sorted(train_rating_raw['movieId'].drop_duplicates().tolist())

    user_item_df = pd.DataFrame(None, index=user_list, columns=movie_list)
    item_item_df = pd.DataFrame(0.00, index=movie_list, columns=movie_list)

    for i, each in train_rating_raw.iterrows():
        user_item_df.at[int(each['userId']), int(
            each['movieId'])] = each['rating']

    return user_item_df, item_item_df

# 计算 item 相似度 方法


def correlation_pearson_based(user_item_df, item_item_df):

    items = item_item_df.columns
    users = user_item_df.index
    # 计算 item 评分均值

    item_mean_df = user_item_df.mean()
    for i in items:
        for j in items:
            # 分子
            R = 0
            # 分母
            R_i = 0
            R_j = 0

            if i == j:
                item_item_df.at[i, j] = 1.0
            else:
                for u in users:
                    if user_item_df.at[u, i] and user_item_df.at[u, j]:
                        R_u_i = user_item_df.at[u, i] - item_mean_df.at[i]
                        R_u_j = user_item_df.at[u, j] - item_mean_df.at[j]
                        R_i += R_u_i ** 2
                        R_j += R_u_j ** 2
                        R += R_u_i * R_u_j
                item_item_df.at[i, j] = R / \
                    (np.power(R_i, 0.5)*np.power(R_j, 0.5))
    return item_item_df


def adjust_cosine(user_item_df, item_item_df):

    items = item_item_df.columns
    users = user_item_df.index
    # 计算 user 评分均值

    user_mean_df = user_item_df.mean(1)

    for i in items:
        for j in items:
            # 分子
            R = 0
            # 分母
            R_i = 0
            R_j = 0

            if i == j:
                item_item_df.at[i, j] = 1.0
            else:
                for u in users:
                    if user_item_df.at[u, i] and user_item_df.at[u, j]:
                        R_u_i = user_item_df.at[u, i] - user_mean_df.at[i]
                        R_u_j = user_item_df.at[u, j] - user_mean_df.at[j]
                        R_i += R_u_i ** 2
                        R_j += R_u_j ** 2
                        R += R_u_i * R_u_j
                item_item_df.at[i, j] = R / \
                    (np.power(R_i, 0.5)*np.power(R_j, 0.5))
    return item_item_df

# 根据 item-item相似度  推荐


def item_CF(userId, item_item_df, top_k):
    pass

user_item_df, item_item_df = user_item_table(
    'temp/demo.csv')
