# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFameta(RPackage):
	"""Fatty Acid Metabolic Analysis

	Fatty acid metabolic analysis aimed to the estimation of FA import (I), de novo synthesis (S), fractional contribution of the 13C-tracers (D0, D1, D2), elongation (E) and desaturation (Des) based on mass isotopologue data.
	"""
	
	cran = "FAMetA" 

	version("0.1.6", md5="73545a711f93f2678343e70ba39d5a4c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lipidms@3.0.4:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-accucor", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
