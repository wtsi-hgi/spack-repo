# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFabinference(RPackage):
	"""FAB p-Values and Confidence Intervals

	Frequentist assisted by Bayes (FAB) p-values and confidence 
 interval construction. See 
 Hoff (2019) <arXiv:1907.12589> 
 "Smaller p-values via indirect information",
 Hoff and Yu (2019) <doi:10.1214/18-EJS1517> 
 "Exact adaptive confidence intervals for linear regression coefficients", and
 Yu and Hoff (2018) <doi:10.1093/biomet/asy009> 
 "Adaptive multigroup confidence intervals with constant coverage".
	"""
	
	cran = "FABInference" 

	version("0.1", md5="2b7edfa65a187f0389c85f5ce64d83b5")

	depends_on("r-mass", type=("build", "run"))
