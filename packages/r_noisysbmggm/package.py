# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoisysbmggm(RPackage):
	"""Noisy Stochastic Block Model for GGM Inference

	Greedy Bayesian algorithm to fit the noisy stochastic block model to an observed sparse graph. Moreover, a graph inference procedure to recover Gaussian Graphical Model (GGM) from real data. This procedure comes with a control of the false discovery rate. The method is described in the article "Enhancing the Power of Gaussian Graphical Model Inference by Modeling the Graph Structure" by Kilian, Rebafka, and Villers (2024) <arXiv:2402.19021>.
	"""
	
	cran = "noisysbmGGM" 

	version("0.1.2.3", md5="a15dc39ce66635ada4e7b05d9f8860c6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-silggm", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
