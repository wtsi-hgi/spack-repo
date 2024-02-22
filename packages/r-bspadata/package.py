# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBspadata(RPackage):
	"""Bayesian Proposal to Fit Spatial Econometric Models

	The purpose of this package is to fit the three Spatial Econometric Models proposed
  in Anselin (1988, ISBN:9024737354) in the homoscedastic and the heteroscedatic case. The fit is made through MCMC algorithms
  and observational working variables approach.
	"""
	
	cran = "BSPADATA" 

	version("1.1.0", md5="3f3b6c87c323b6c009571882a296a2fd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
