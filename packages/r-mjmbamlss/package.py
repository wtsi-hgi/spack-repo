# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMjmbamlss(RPackage):
	"""Multivariate Joint Models with 'bamlss'

	Multivariate joint models of longitudinal and time-to-event data based on functional principal components implemented with 'bamlss'. Implementation for Volkmann, Umlauf, Greven (2023) <arXiv:2311.06409>.
	"""
	
	cran = "MJMbamlss" 

	version("0.1.0", md5="4ae3cdbe66625acdb2e4123b2fa4b348")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-bamlss", type=("build", "run"))
	depends_on("r-fundata", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-gamm4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-refund", type=("build", "run"))
	depends_on("r-fdapace", type=("build", "run"))
	depends_on("r-sparseflmm", type=("build", "run"))
	depends_on("r-mfpca", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
