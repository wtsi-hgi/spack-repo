# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeepnn(RPackage):
	"""Deep Learning

	Implementation of some Deep Learning methods. Includes multilayer perceptron, different activation functions, regularisation strategies, stochastic gradient descent and dropout. Thanks go to the following references for helping to inspire and develop the package: Ian Goodfellow, Yoshua Bengio, Aaron Courville, Francis Bach (2016, ISBN:978-0262035613) Deep Learning. Terrence J. Sejnowski (2018, ISBN:978-0262038034) The Deep Learning Revolution. Grant Sanderson (3brown1blue) <https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi> Neural Networks YouTube playlist. Michael A. Nielsen <http://neuralnetworksanddeeplearning.com/> Neural Networks and Deep Learning.
	"""
	
	cran = "deepNN" 

	version("1.2", md5="752189acead301b55c409453af58fe1e")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
