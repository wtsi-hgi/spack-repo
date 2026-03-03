# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmFuzzy(RPackage):
	"""EM Algorithm for Maximum Likelihood Estimation by Non-Precise
Information

	The EM algorithm is a powerful tool for computing maximum likelihood estimates with incomplete data. This package will help to applying EM algorithm based on triangular and trapezoidal fuzzy numbers (as two kinds of incomplete data). A method is proposed for estimating the unknown parameter in a parametric statistical model when the observations are triangular or trapezoidal fuzzy numbers. This method is based on maximizing the observed-data likelihood defined as the conditional probability of the fuzzy data; for more details and formulas see Denoeux (2011) <doi:10.1016/j.fss.2011.05.022>.
	"""
	
	cran = "EM.Fuzzy" 

	version("1.0", md5="fb55f479e3cc667fe2026314c236dec6")

	depends_on("r-fuzzynumbers", type=("build", "run"))
	depends_on("r-distrib", type=("build", "run"))
