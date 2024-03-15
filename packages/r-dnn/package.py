# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnn(RPackage):
	"""Deep Neural Network Tools for Probability and Statistic Models

	Contains tools to build deep neural network with flexible users define loss function and probability models. Several applications included in this package are, 1) The (deepAFT) model, a deep neural network model for accelerated failure time (AFT) model for survival data. 2) The (deepGLM) model, a deep neural network model for generalized linear model (glm) for continuous, categorical and Poisson data.
	"""
	
	cran = "dnn" 

	version("0.0.6", md5="4fb49f3dcbb14ed68eebec6e368c108f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
