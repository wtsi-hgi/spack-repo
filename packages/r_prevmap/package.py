# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrevmap(RPackage):
	"""Geostatistical Modelling of Spatially Referenced Prevalence Data

	Provides functions for both likelihood-based
    and Bayesian analysis of spatially referenced prevalence data. For a tutorial on the use of the R package, see Giorgi and Diggle (2017) <doi:10.18637/jss.v078.i08>.
	"""
	
	cran = "PrevMap" 

	version("1.5.4", md5="8264bfc85a7e9536a554e844092b006d")

	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
