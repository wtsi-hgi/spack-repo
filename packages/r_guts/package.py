# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuts(RPackage):
	"""Fast Calculation of the Likelihood of a Stochastic Survival
Model

	Given exposure and survival time series as well as parameter values, GUTS allows for the fast calculation of the survival probabilities as well as the logarithm of the corresponding likelihood (see Albert, C., Vogel, S. and Ashauer, R. (2016) <doi:10.1371/journal.pcbi.1004978>).
	"""
	
	cran = "GUTS" 

	version("1.2.5", md5="4508c7d73af5a56c709e3777d5ffaa50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
