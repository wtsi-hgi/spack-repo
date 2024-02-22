# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrat(RPackage):
	"""An Implementation of the Stratification Index

	An implementation of the stratification index proposed by Zhou (2012) <DOI:10.1177/0081175012452207>.
  The package provides two functions, srank, which returns stratum-specific
  information, including population share and average percentile rank; and strat,
  which returns the stratification index and its approximate standard error.
  When a grouping factor is specified, strat also provides a detailed decomposition
  of the overall stratification into between-group and within-group components.
	"""
	
	homepage = "https://github.com/xiangzhou09/strat"
	cran = "strat" 

	version("0.1", md5="55066ed17f0e58e2f755547ba4d9e973")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-hmisc@4.0.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
