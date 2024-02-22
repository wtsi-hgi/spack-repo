# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwoxtwo(RPackage):
	"""Work with Two-by-Two Tables

	A collection of functions for data analysis with two-by-two contingency tables. The package provides tools to compute measures of effect (odds ratio, risk ratio, and risk difference), calculate impact numbers and attributable fractions, and perform hypothesis testing. Statistical analysis methods are oriented towards epidemiological investigation of relationships between exposures and outcomes.
	"""
	
	cran = "twoxtwo" 

	version("0.1.0", md5="f4cd69934f3366266c762f5cef48f2d4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
