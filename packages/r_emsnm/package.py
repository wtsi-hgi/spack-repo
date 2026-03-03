# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmsnm(RPackage):
	"""EM Algorithm for Sigmoid Normal Model

	It provides a method based on EM algorithm to estimate the parameter of a mixture model, Sigmoid-Normal Model, where the samples come from several normal distributions (also call them subgroups) whose mean is determined by co-variable Z and coefficient alpha while the variance are homogeneous. Meanwhile, the subgroup each item belongs to is determined by co-variables X and coefficient eta through Sigmoid link function which is the extension of Logistic Link function. It uses bootstrap to estimate the standard error of parameters. When sample is indeed separable, removing estimation with abnormal sigma, the estimation of alpha is quite well. I used this method to explore the subgroup structure of HIV patients and it can be used in other domains where exists subgroup structure.
	"""
	
	cran = "EMSNM" 

	version("1.0", md5="c32e9d8211f84993bdb3de63f722291f")

