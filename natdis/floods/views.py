# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import numpy as np
from django.http import HttpResponse
import tensorflow as tf
from keras.models import Model 
from keras import optimizers
from keras.models import load_model

def index(request):
	return render(request, 'floods/index.html')

def predict(request):

	if request.method == 'POST':
		minitemp = request.POST['minitemp']
		maxitemp = request.POST['maxitemp']
		windgust = request.POST['windgust']
		wind9 = request.POST['wind9']
		wind3 = request.POST['wind3']
		humid9 = request.POST['humid9']
		humid3 = request.POST['humid3']
		pressure9 = request.POST['pressure9']
		pressure3 = request.POST['pressure3']
		temp9 = request.POST['temp9']
		temp3 = request.POST['temp3']

		model = load_model('Model.h5')
		optimizer = tf.train.RMSPropOptimizer(0.002)
		model.compile(loss='mse',
		            optimizer=optimizer,
		            metrics=['accuracy'])

		pridection = np.array([minitemp,maxitemp,windgust,wind9,wind3,humid9,humid3,pressure9,pressure3,temp9,temp3])

		mean = np.array([12.068963,23.009951,37.19739,13.88135,18.25159,67.70561,49.9628,911.645197,909.72206092,16.76982,21.128429])
		std = np.array([6.47953722,7.41225215,16.68598056,9.01179628,9.14530111,20.95509877,22.34781323,310.98021687,309.95752359,6.71328472,7.64915217])
		pridection = (pridection - mean) / std

		if (pridection.ndim == 1):
		    pridection = np.array([pridection])

		rainfall = model.predict(pridection)

		floods = (rainfall - 5) * 5

		if (floods > 100):
		    floods = 100

		text = "Floods will occur, take necessary precautions."

		return render(request, 'floods/results.html',{'rainfall':rainfall,'floods':floods, 'text':text})

	else:
		return render(request, 'floods/predict.html')

def manage(request):
	return render(request, 'floods/manage.html')
