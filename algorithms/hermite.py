#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Hermite插值

#基函数求导
def DerivLagrange(i, lPoints):
	iLen = len(lPoints)
	result = 0.0

	for j in range(iLen):
		if i != j:
			result += 1.0 / (lPoints[i][0] - lPoints[j][0])
	return result

#计算基函数值
def Lagrange(i, lPoints, x):
	iLen = len(lPoints)
	result = 1.0 

	for j in range(iLen):
		if i != j:
			result *= (x - lPoints[j][0])
			result /= (lPoints[i][0] - lPoints[j][0])
	return result

def NormalHermite(lPoints, lDeriv=[]):
	iLen = len(lPoints)
	iDev = len(lDeriv)
	if iLen > iDev:
		lDv = [0 for _ in range(iLen - iDev)]
		lDeriv.extend(lDv)
	def Hermite(x):
		result = 0.0 
		for i in range(iLen):
			result += (lPoints[i][1] + (x - lPoints[i][0]) * (lDeriv[i] - 2 * lPoints[i][1] * DerivLagrange(i, lPoints))) * (Lagrange(i, lPoints, x) ** 2)
		return result
	return Hermite


