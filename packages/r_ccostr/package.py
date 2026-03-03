# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcostr(RPackage):
	"""Estimation of Mean Costs in Censored Data

	Implementation of estimators for inferring 
    the mean of censored cost data. Including the estimators
    BT from Bang and Tsiatis (2000) <doi:10.1093/biomet/87.2.329> and 
    ZT from Zhao and Tian (2001) <doi:10.1111/j.0006-341X.2001.01002.x>.
	"""
	
	cran = "ccostr" 

	version("0.1.0", md5="29e6659a7340297f91f04e8b707126d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
