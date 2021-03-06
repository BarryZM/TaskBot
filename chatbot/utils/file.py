# -*- coding: utf-8 -*-
# @Time    : 5/11/18 14:16
# @Author  : evilpsycho
# @Mail    : evilpsycho42@gmail.com
import json
import pickle


def read_json(fpath):
    with open(fpath) as fin:
        return json.load(fin)


def save_json(data, fpath):
    with open(fpath, 'w') as fout:
        return json.dump(data, fout)


def save_pickle(data, fpath):
    with open(fpath, 'wb') as fout:
        pickle.dump(data, fout)


def load_pickle(fpath):
    with open(fpath, 'rb') as fin:
        return pickle.load(fin)