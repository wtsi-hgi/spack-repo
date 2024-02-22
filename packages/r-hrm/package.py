# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHrm(RPackage):
	"""High-Dimensional Repeated Measures

	Methods for testing main and interaction effects in possibly
    high-dimensional parametric or nonparametric repeated measures in factorial designs for univariate or multivariate data.
    The observations of the subjects are assumed to be multivariate normal if using the parametric test.
    The nonparametric version tests with regard to nonparametric relative effects (based on pseudo-ranks).
    It is possible to use up to 2 whole- and 3 subplot factors.
	"""
	
	homepage = "http://github.com/happma/HRM"
	cran = "HRM" 

	version("1.2.1", md5="3b39a707c87c556e6880be0e8e3ff073")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doby", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pseudorank@0.3.8:", type=("build", "run"))
