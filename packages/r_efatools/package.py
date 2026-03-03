# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REfatools(RPackage):
	"""Fast and Flexible Implementations of Exploratory Factor Analysis
Tools

	Provides functions to perform exploratory factor analysis (EFA) procedures and compare their solutions. The goal is to provide state-of-the-art factor retention methods and a high degree of flexibility in the EFA procedures. This way, for example, implementations from R 'psych' and 'SPSS' can be compared. Moreover, functions for Schmid-Leiman transformation and the computation of omegas are provided. To speed up the analyses, some of the iterative procedures, like principal axis factoring (PAF), are implemented in C++.
	"""
	
	homepage = "https://github.com/mdsteiner/EFAtools"
	cran = "EFAtools" 

	version("0.4.4", md5="aff56d9d142923e0b00dd73a55b7a241")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
