# -*- coding: utf-8 -*-
# @Author  : Shajiu
# @FileName: app.py
# @Time    : 2021/8/22 17:18
from flask import Flask, render_template
from data import *

app = Flask(__name__)


@app.route('/')
def index():
    data = SourceData()
    return render_template('index.html', form=data, title=data.title)


@app.route('/corp')
def corp():
    data = CorpData()
    return render_template('index.html', form=data, title=data.title)


@app.route('/job')
def job():
    data = JobData()
    return render_template('index.html', form=data, title=data.title)


if __name__ == "__main__":
    app.run(host='127.1.1.1', debug=False)
