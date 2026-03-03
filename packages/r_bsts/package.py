# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsts(RPackage):
	"""Bayesian Structural Time Series

	Time series regression using dynamic linear models fit using
  MCMC. See Scott and Varian (2014) <DOI:10.1504/IJMMNO.2014.059942>, among many
  other sources.
	"""
	
	cran = "bsts" 

	version("0.9.10", md5="3584741674e464f7349f8b7996891259")

	depends_on("r-boomspikeslab@1.2.6:", type=("build", "run"))
	depends_on("r-zoo@1.8:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-boom@0.9.13:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
