# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLillies(RPackage):
	"""Estimation of Life Years Lost

	Estimation of life expectancy and
    Life Years Lost (LYL, or lillies for short) for a given population, for 
    example those with a given disease or condition. In addition, the package 
    can be used to compare estimates from different populations, or to estimate 
    confidence intervals. Technical details of the method are available in
    Plana-Ripoll et al. (2020) <doi:10.1371/journal.pone.0228073> and Andersen
    (2017) <doi:10.1002/sim.7357>.
	"""
	
	cran = "lillies" 

	version("0.2.12", md5="d6aee4ee0c564cc551725d62b36fe8a1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
