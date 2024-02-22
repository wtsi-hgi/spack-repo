# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKriginv(RPackage):
	"""Kriging-Based Inversion for Deterministic and Noisy Computer
Experiments

	Criteria and algorithms for sequentially estimating level sets of a multivariate numerical function, possibly observed with noise.
	"""
	
	homepage = "https://doi.org/10.1016/j.csda.2013.03.008"
	cran = "KrigInv" 

	version("1.4.2", md5="7c3946a175edf316d2f59569763dc92f")

	depends_on("r-dicekriging", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
	depends_on("r-anmc", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
