# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvsacim(RPackage):
	"""Structural Additive Cumulative Intensity Models with IV

	An instrumental variable estimator under structural cumulative additive intensity model is fitted, that leverages initial randomization as the IV. The estimator can be used to fit an additive hazards model under time to event data which handles treatment switching (treatment crossover) correctly. We also provide a consistent variance estimate.
	"""
	
	cran = "ivsacim" 

	version("2.1.0", md5="97cbc26060d9bc33251630ed6f7aa026")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
