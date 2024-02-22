# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFglsnet(RPackage):
	"""A Feasible Generalized Least Squares Estimator for Regression
Analysis of Outcomes with Network Dependence

	The function estimates a multivariate regression model for outcomes with network dependence.
	"""
	
	cran = "fglsnet" 

	version("1.0", md5="c2829d6c34b85a7ecd97939c5be3bae1")

	depends_on("r-network", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
