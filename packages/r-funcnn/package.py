# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuncnn(RPackage):
	"""Functional Neural Networks

	A collection of functions which fit functional neural network models. In
            other words, this package will allow users to build deep learning models 
            that have either functional or scalar responses paired with functional and 
            scalar covariates. We implement the theoretical discussion found 
            in Thind, Multani and Cao (2020) <arXiv:2006.09590> through the help of a main fitting and 
            prediction function as well as a number of helper functions to assist with 
            cross-validation, tuning, and the display of estimated functional weights.
	"""
	
	homepage = "https://arxiv.org/abs/2006.09590"
	cran = "FuncNN" 

	version("1.0", md5="ba11ed65e11b41d6fcd55ca931d9cc28")

	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-flux", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
