#!/usr/bin/python3
# -*- coding: utf-8 -*-
#拉格朗日插值法

def Lagrange(lPoints):
	iLen = len(lPoints)
	def innerLagrange(x):
		value = 0.0
		for idx in range(iLen):
			xi, yi = lPoints[idx]
			top, bottom = 1.0, 1.0
			for i in range(iLen):
				if idx == i:
					continue
				yi = yi * (x - lPoints[i][0])
				yi = yi / (xi - lPoints[i][0])
			value += yi
		return value
	return innerLagrange




