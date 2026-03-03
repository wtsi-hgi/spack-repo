# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RL2densitygoftest(RPackage):
	"""Density Goodness-of-Fit Test

	Provides functions for the implementation of a density goodness-of-fit test, based on piecewise approximation of the L2 distance.
	"""
	
	cran = "L2DensityGoFtest" 

	version("0.6.0", md5="0ae8401732ac0edfedc92e2d9a7dee64")

	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-nor1mix", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
