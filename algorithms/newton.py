#!/usr/bin/python3
# -*- coding: utf-8 -*-
#牛顿插值

def CalChaShang(n, lPoints):
	f, temp = 0, 0
	for idx in range(0, n+1):
		temp = lPoints[idx][1]
		for i in range(0, n+1):
			if idx != i:
				temp /= (lPoints[idx][0] - lPoints[i][0])
		f += temp 
	return f

def Newton(lPoints, x):
	result = 0 
	iLen = len(lPoints)
	for idx in range(iLen):
		temp = 1 
		f = CalChaShang(idx, lPoints)
		for i in range(idx):
			temp = temp * (x - lPoints[i][0])
		result += f * temp
	return result