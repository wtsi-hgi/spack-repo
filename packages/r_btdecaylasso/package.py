# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBtdecaylasso(RPackage):
	"""Bradley-Terry Model with Exponential Time Decayed Log-Likelihood
and Adaptive Lasso

	We utilize the Bradley-Terry Model to estimate the abilities of teams using paired comparison data. For dynamic approximation of current rankings, we employ the Exponential Decayed Log-likelihood function, and we also apply the Lasso penalty for variance reduction and grouping. The main algorithm applies the Augmented Lagrangian Method described by Masarotto and Varin (2012) <doi:10.1214/12-AOAS581>.
	"""
	
	cran = "BTdecayLasso" 

	version("0.1.1", md5="90dcd3fd05d7b28f1abc1693d4862ca5")

	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
