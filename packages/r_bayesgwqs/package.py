# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesgwqs(RPackage):
	"""Bayesian Grouped Weighted Quantile Sum Regression

	Fits Bayesian grouped weighted quantile sum (BGWQS) regressions for one or more chemical groups with binary outcomes. Wheeler DC et al. (2019) <doi:10.1016/j.sste.2019.100286>.
	"""
	
	cran = "BayesGWQS" 

	version("0.1.1", md5="c050a14ebdffe7f876a1cc3f8d897b62")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
