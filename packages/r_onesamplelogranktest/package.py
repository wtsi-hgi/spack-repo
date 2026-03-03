# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnesamplelogranktest(RPackage):
	"""One-Sample Log-Rank Test

	The log-rank test is performed to assess the survival outcomes between two group. 
             When there is no proper control group or obtaining such data is cumbersome, one sample
             log-rank test can be applied. This package performs one sample log-rank test as described in Finkelstein et al. (2003)<doi:10.1093/jnci/djt227> and variation of the 
             test for small sample sizes which is detailed in FD Liddell (1984)<doi:10.1136/jech.38.1.85> paper. Visualization function in the package
             generates Kaplan-Meier Curve comparing survival curve of the general population against that of the population of interest.
	"""
	
	cran = "OneSampleLogRankTest" 

	version("0.9.2", md5="c75b399226ae1e311e23620c1c852fb3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
