# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeuralsens(RPackage):
	"""Sensitivity Analysis of Neural Networks

	Analysis functions to quantify inputs importance in neural network models.
  Functions are available for calculating and plotting the inputs importance and obtaining
  the activation function of each neuron layer and its derivatives. The importance of a given
  input is defined as the distribution of the derivatives of the output with respect to that
  input in each training data point <doi:10.18637/jss.v102.i07>.
	"""
	
	homepage = "https://github.com/JaiPizGon/NeuralSens"
	cran = "NeuralSens" 

	version("1.1.2", md5="edd5e17c2642bd408aa31c881eaab094")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-neuralnettools", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggbreak", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
