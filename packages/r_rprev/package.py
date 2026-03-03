# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRprev(RPackage):
	"""Estimating Disease Prevalence from Registry Data

	Estimates disease prevalence for a given index date using existing
    registry data extended with Monte Carlo simulations following the method of Crouch et al (2014) <doi: 10.1016/j.canep.2014.02.005>.
	"""
	
	homepage = "https://github.com/stulacy/rprev-dev"
	cran = "rprev" 

	version("1.0.5", md5="32db0584c19ddd23472f8f74e7eecd69")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
