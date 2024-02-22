# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtmcmove(RPackage):
	"""Modeling Animal Movement with Continuous-Time Discrete-Space
Markov Chains

	Software to facilitates taking movement data in xyt format and pairing it with raster covariates within a continuous time Markov chain (CTMC) framework.  As described in Hanks et al. (2015) <DOI:10.1214/14-AOAS803> , this allows flexible modeling of movement in response to covariates (or covariate gradients) with model fitting possible within a Poisson GLM framework. 
	"""
	
	cran = "ctmcmove" 

	version("1.2.9", md5="f727a9603b759002998d1eed1ec8e00b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-gdistance", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
