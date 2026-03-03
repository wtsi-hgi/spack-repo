# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetterreg(RPackage):
	"""Better Statistics for OLS and Binomial Logistic Regression

	Provides squared semi partial correlations, tolerance, Mahalanobis, Likelihood Ratio Chi Square, and Pseudo R Square. Aberson, C. L. (2022) <doi:10.31234/osf.io/s2yqn>.
	"""
	
	cran = "BetterReg" 

	version("0.2.0", md5="6aeca56b54e4aa7977a909e65f763935")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car@3.0.0:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
