# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCensmfm(RPackage):
	"""Finite Mixture of Multivariate Censored/Missing Data

	It fits finite mixture models for censored or/and missing data using several multivariate distributions. Point estimation and asymptotic inference (via empirical information matrix) are offered as well as censored data generation. Pairwise scatter and contour plots can be generated. Possible multivariate distributions are the well-known normal, Student-t and skew-normal distributions. This package is an complement of Lachos, V. H., Moreno, E. J. L., Chen, K. & Cabral, C. R. B. (2017) <doi:10.1016/j.jmva.2017.05.005> for the multivariate skew-normal case. 
	"""
	
	cran = "CensMFM" 

	version("3.0", md5="9ea4c07f61242769f775f1a3f4dc2e37")

	depends_on("r-momtrunc@5.87:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.11:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tlrmvnmvt@1.1:", type=("build", "run"))
