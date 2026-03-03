# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsm(RPackage):
	"""Density Surface Modelling of Distance Sampling Data

	Density surface modelling of line transect data. A Generalized
    Additive Model-based approach is used to calculate spatially-explicit estimates
    of animal abundance from distance sampling (also presence/absence and strip
    transect) data. Several utility functions are provided for model checking,
    plotting and variance estimation.
	"""
	
	homepage = "https://github.com/DistanceDevelopment/dsm"
	cran = "dsm" 

	version("2.3.3", md5="0d89579f31e7275b0489b9f3ce6895bc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mgcv@1.8.23:", type=("build", "run"))
	depends_on("r-mrds@2.1.16:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
