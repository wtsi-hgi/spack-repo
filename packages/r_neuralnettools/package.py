# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeuralnettools(RPackage):
	"""Visualization and Analysis Tools for Neural Networks

	Visualization and analysis tools to aid in the interpretation of
    neural network models.  Functions are available for plotting,
    quantifying variable importance, conducting a sensitivity analysis, and
    obtaining a simple list of model weights.
	"""
	
	cran = "NeuralNetTools" 

	version("1.5.3", md5="722f47f014194afdd18ea5c522848be5")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
