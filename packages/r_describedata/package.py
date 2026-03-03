# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescribedata(RPackage):
	"""Miscellaneous Descriptive Functions

	
  Helper functions for descriptive tasks such as making print-friendly bivariate 
  tables, sample size flow counts, and visualizing sample distributions. Also 
  contains 'R' approximations of some common 'SAS' and 'Stata' functions such 
  as 'PROC MEANS' from 'SAS' and 'ladder', 'gladder', and 'pwcorr' from 'Stata'.
	"""
	
	cran = "describedata" 

	version("0.1.0", md5="e6977c7aaf59465cf3639f12d1cfb52c")

	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
