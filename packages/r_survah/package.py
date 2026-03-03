# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvah(RPackage):
	"""Survival Data Analysis using Average Hazard

	Performs two-sample comparisons based on average hazard with survival weight (AHSW) or general censoring-free incidence rate (CFIR) proposed by Uno and Horiguchi (2023) <doi:10.1002/sim.9651>.
	"""
	
	cran = "survAH" 

	version("1.0.0", md5="25f34a71b093e91af09b083db6df0e80")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
