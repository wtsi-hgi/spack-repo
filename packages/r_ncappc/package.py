# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcappc(RPackage):
	"""NCA Calculations and Population Model Diagnosis

	A flexible tool that can perform
    (i) traditional non-compartmental analysis (NCA) and
    (ii) Simulation-based posterior predictive checks for population
    pharmacokinetic (PK) and/or pharmacodynamic (PKPD) models using NCA metrics. 
	"""
	
	cran = "ncappc" 

	version("0.3.0", md5="5cc80b6e6869114d17e56765f137900e")

	depends_on("r@2.15.3:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
	depends_on("r-readr@0.2.2:", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-poped", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
