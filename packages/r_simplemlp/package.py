# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplemlp(RPackage):
	"""Simple Multilayer Perceptron Neural Network

	Create and train a multilayer perceptron, a type of feedforward, 
    fully connected neural network. Features 2 ReLU hidden layers. Learn more 
    about about the activation functions and backpropagation used by this 
    network in Goodfellow et al. (2016, ISBN: 9780262035613) "Deep Learning".
	"""
	
	cran = "simpleMLP" 

	version("1.0.0", md5="a26c960a3afd67ee1edcf68d2cbbe66c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
