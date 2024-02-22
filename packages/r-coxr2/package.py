# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxr2(RPackage):
	"""R-Squared Measure Based on Partial LR Statistic, for the Cox PH
Regression Model

	Calculate the R-squared, aka explained randomness, based on the partial likelihood ratio statistic under the Cox Proportional Hazard model [J O'Quigley, R Xu, J Stare (2005) <doi:10.1002/sim.1946>].
	"""
	
	cran = "CoxR2" 

	version("1.0", md5="8677a89f106650e86e6bc2840f5f1ccb", url="https://cran.r-project.org/src/contrib/CoxR2_1.0.tar.gz")

	depends_on("r-survival", type=("build", "run"))
