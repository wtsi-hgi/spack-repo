# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrosscarry(RPackage):
	"""Analysis of Data from a Crossover Design with GEE

	Analyze data from a crossover design using generalized estimation equations (GEE), including carryover effects and various correlation structures based on the Kronecker product. It contains functions for semiparametric estimates of carry-over effects in repeated measures and allows estimation of complex carry-over effects. Related work includes: a) Cruz N.A., Melo O.O., Martinez C.A. (2023). "CrossCarry: An R package for the analysis of data from a crossover design with GEE". <arXiv:2304.02440v1>. b)  Cruz N.A., Melo O.O., Martinez C.A. (2023). "A correlation structure for the analysis of Gaussian and non-Gaussian responses in crossover experimental designs with repeated measures". <doi:10.1007/s00362-022-01391-z> and c) Cruz N.A., Melo O.O., Martinez C.A. (2023). "Semiparametric generalized estimating equations for repeated measurements in cross-over designs". <doi:10.1177/09622802231158736>.
	"""
	
	cran = "CrossCarry" 

	version("0.1.0", md5="68cdf7d2f479d708b60c1427aa287f17")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gee", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
