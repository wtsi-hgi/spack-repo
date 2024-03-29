# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdmonreg(RPackage):
	"""Compute least squares estimates of one bounded or two ordered
isotonic regression curves

	We consider the problem of estimating two isotonic regression curves g1* and g2* under the constraint that they are ordered, i.e. g1* <= g2*. Given two sets of n data points y_1, ..., y_n and z_1, ..., z_n that are observed at (the same) deterministic design points x_1, ..., x_n, the estimates are obtained by minimizing the Least Squares criterion L(a, b) = sum_{i=1}^n (y_i - a_i)^2 w1(x_i) + sum_{i=1}^n (z_i - b_i)^2 w2(x_i) over the class of pairs of vectors (a, b) such that a and b are isotonic and a_i <= b_i for all i = 1, ..., n. We offer two different approaches to compute the estimates: a projected subgradient algorithm where the projection is calculated using a PAVA as well as Dykstra's cyclical projection algorithm.
	"""
	
	homepage = "http://www.ceremade.dauphine.fr/~fadoua"
	cran = "OrdMonReg" 

	version("1.0.3", md5="544320e7e3891f45ddb48d6c11975e2c")

