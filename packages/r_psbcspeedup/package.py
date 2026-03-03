# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsbcspeedup(RPackage):
	"""Penalized Semiparametric Bayesian Cox Models

	Algorithms to speed up the Bayesian Lasso Cox model (Lee et al., Int J Biostat, 2011 <doi:10.2202/1557-4679.1301>) and the Bayesian Lasso Cox with mandatory variables (Zucknick et al. Biometrical J, 2015 <doi:10.1002/bimj.201400160>).
	"""
	
	homepage = "https://github.com/ocbe-uio/psbcSpeedUp"
	cran = "psbcSpeedUp" 

	version("2.0.6", md5="5d69d7eca1eab0d2d906195dffe93417")
	version("2.0.5", md5="02ba52f739c100d10507ef3a7b78cdaa")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-riskregression", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9:", type=("build", "run"))
