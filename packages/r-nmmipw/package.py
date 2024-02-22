# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmmipw(RPackage):
	"""Inverse Probability Weighting under Non-Monotone Missing

	We fit inverse probability weighting estimator and the augmented inverse probability weighting for non-monotone missing at random data. 
	"""
	
	cran = "NMMIPW" 

	version("0.1.0", md5="60d14ba140bcbb820cb49cbd9b9fc765")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lava", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
