# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBp(RPackage):
	"""Blood Pressure Analysis in R

	A comprehensive package to aid in the analysis of blood pressure data of all forms by providing both descriptive and visualization tools for researchers.
	"""
	
	homepage = "https://github.com/johnschwenck/bp"
	cran = "bp" 

	version("2.1.0", md5="73726aaa4d71821b45c3b21ecebed3e3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
