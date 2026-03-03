# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcpan(RPackage):
	"""Multiple Comparisons Using Normal Approximation

	Multiple contrast tests and simultaneous confidence
 intervals based on normal approximation. With implementations for
 binomial proportions in a 2xk setting (risk difference and odds ratio),
 poly-3-adjusted tumour rates, biodiversity indices (multinomial data) 
 and expected values under lognormal assumption. Approximative power 
 calculation for multiple contrast tests of binomial and Gaussian data.
	"""
	
	cran = "MCPAN" 

	version("1.1-21", md5="8c582c6c55721a3c1fcfdcd0541f800f")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
