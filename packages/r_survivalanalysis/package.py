# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvivalanalysis(RPackage):
	"""High-Level Interface for Survival Analysis and Associated Plots

	A high-level interface to perform survival analysis, 
    including Kaplan-Meier analysis and log-rank tests and Cox regression.
    Aims at providing a clear and elegant syntax, support for use in a pipeline, structured output and plotting.
    Builds upon the 'survminer' package for Kaplan-Meier plots and provides
    a customizable implementation for forest plots.
    Kaplan & Meier (1958) <doi:10.1080/01621459.1958.10501452>
    Cox (1972) <JSTOR:2985181>
    Peto & Peto (1972) <JSTOR:2344317>.
	"""
	
	cran = "survivalAnalysis" 

	version("0.3.0", md5="805c34fb30e653e3de362d8fe3da1ddf")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-survminer@0.4:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-tidytidbits", type=("build", "run"))
