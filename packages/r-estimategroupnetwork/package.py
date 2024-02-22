# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstimategroupnetwork(RPackage):
	"""Perform the Joint Graphical Lasso and Selects Tuning Parameters

	Can be used to simultaneously estimate networks (Gaussian Graphical Models) in data from different groups or classes via Joint Graphical Lasso. Tuning parameters are selected via information criteria (AIC / BIC / extended BIC) or cross validation.
	"""
	
	cran = "EstimateGroupNetwork" 

	version("0.3.1", md5="43b70cbe6605500f961eb0c50aee39fd")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
