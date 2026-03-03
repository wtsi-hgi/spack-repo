# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantilegh(RPackage):
	"""Quantile Least Mahalanobis Distance Estimator for Tukey g-&-h
Mixture

	Functions for simulation, estimation, and model
       selection of finite mixtures of Tukey's g-and-h
       distributions.
	"""
	
	cran = "QuantileGH" 

	version("0.1.5", md5="97f5f3ee1b3f5fb032a7fed0efd9ab68")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-goftest", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-rstpm2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tclust", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
