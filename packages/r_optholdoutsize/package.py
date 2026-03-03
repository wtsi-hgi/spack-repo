# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptholdoutsize(RPackage):
	"""Estimation of Optimal Size for a Holdout Set for Updating a
Predictive Score

	Predictive scores must be updated with care, because actions taken on the basis of existing risk scores causes bias in risk estimates from the updated score. A holdout set is a straightforward way to manage this problem: a proportion of the population is 'held-out' from computation of the previous risk score. This package provides tools to estimate a size for this holdout set and associated errors. Comprehensive vignettes are included. Please see: Haidar-Wehbe S, Emerson SR, Aslett LJM, Liley J (2022) <arXiv:2202.06374> for details of methods. 
	"""
	
	cran = "OptHoldoutSize" 

	version("0.1.0.0", md5="6f06916a9a990eae63099d37281baf57")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-mle-tools", type=("build", "run"))
