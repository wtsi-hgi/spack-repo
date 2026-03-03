# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMplikelihoodwb(RPackage):
	"""Modified Profile Likelihood Estimation for Weibull Shape and
Regression Parameters

	Computing modified profile likelihood estimates for Weibull Shape and Regression Parameters. Modified likelihood estimates are provided.
	"""
	
	cran = "MPLikelihoodWB" 

	version("1.1", md5="47a7a1630123066364b732ea80937acb")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r@3.0.2:", type=("build", "run"))
