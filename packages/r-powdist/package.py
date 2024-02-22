# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowdist(RPackage):
	"""Power and Reversal Power Distributions

	Density, distribution function, quantile function and random generation for the family of power and reversal power distributions.
	"""
	
	cran = "powdist" 

	version("0.1.4", md5="3532854e35b5a6d0ddf72ca14f02b90d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-normalp", type=("build", "run"))
