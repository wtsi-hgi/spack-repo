# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeuralgam(RPackage):
	"""Interpretable Neural Network Based on Generalized Additive
Models

	Neural network framework based on Generalized Additive Models from Hastie & Tibshirani (1990, ISBN:9780412343902), which trains a different neural network to estimate the contribution of each feature to the response variable. The networks are trained independently leveraging the local scoring and backfitting algorithms to ensure that the Generalized Additive Model converges and it is additive. The resultant Neural Network is a highly accurate and interpretable deep learning model, which can be used for high-risk AI practices where decision-making should be based on accountable and interpretable algorithms. 
	"""
	
	homepage = "https://inesortega.github.io/neuralGAM/"
	cran = "neuralGAM" 

	version("1.1.0", md5="ec88380b9eee53d0e51e42ae9ddd81fc")

	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("python@3.8.0:", type=("build", "link", "run"))
	depends_on("py-tensorflow", type=("build", "link", "run"))
