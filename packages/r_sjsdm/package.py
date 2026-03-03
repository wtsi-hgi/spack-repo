# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSjsdm(RPackage):
	"""Scalable Joint Species Distribution Modeling

	A scalable method to estimate joint Species Distribution Models (jSDMs) for big community datasets based on a Monte Carlo approximation of the joint likelihood.  The numerical approximation is based on 'PyTorch' and 'reticulate', and can be run on CPUs and GPUs alike. The method is described in Pichler & Hartig (2021) <doi:10.1111/2041-210X.13687>. The package contains various extensions, including support for different response families, ability to account for spatial autocorrelation, and deep neural networks instead of the linear predictor in jSDMs.
	"""
	
	homepage = "https://theoreticalecology.github.io/s-jSDM/"
	cran = "sjSDM" 

	version("1.0.5", md5="96bb72eb59f3fa1e222b383ccccb128b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-ggtern", type=("build", "run"))
