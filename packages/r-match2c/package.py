# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatch2c(RPackage):
	"""Match One Sample using Two Criteria

	Multivariate matching in observational studies typically has two goals: 1. to construct 
    treated and control groups that have similar distribution of observed covariates and 2. to produce 
    matched pairs or sets that are homogeneous in a few priority variables. This packages implements a
    network-flow-based method built around a tripartite graph that can simultaneously achieve both goals.
    The package also implements a template matching algorithm using a variant of the tripartite graph 
    design. A brief description of the workflow and some examples are given in the vignette. A more elaborated
    tutorial can be found at <https://www.researchgate.net/publication/359513837_Tutorial_for_R_Package_match2C>.
	"""
	
	cran = "match2C" 

	version("1.2.4", md5="d95e1234b274e7ca0ca00758181adc3f")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-rcbalance", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
