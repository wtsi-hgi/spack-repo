# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInvgauss(RPackage):
	"""Threshold Regression that Fits the (Randomized Drift) Inverse
Gaussian Distribution to Survival Data

	Fits the (randomized drift) inverse Gaussian distribution to survival data. The model is described in Aalen OO, Borgan O, Gjessing HK. Survival and Event History Analysis. A Process Point of View. Springer, 2008. It is based on describing time to event as the barrier hitting time of a Wiener process, where drift towards the barrier has been randomized with a Gaussian distribution. The model allows covariates to influence starting values of the Wiener process and/or average drift towards a barrier, with a user-defined choice of link functions. 
	"""
	
	homepage = "http://www.uib.no/smis/gjessing/projects/invgauss/"
	cran = "invGauss" 

	version("1.2", md5="450370f96c2d40cdd67a7c1781dfae01")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
