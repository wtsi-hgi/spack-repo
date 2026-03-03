# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginRiskdemo(RPackage):
	"""R Commander Plug-in for Risk Demonstration

	R Commander plug-in to demonstrate various actuarial and financial risks. It includes valuation of bonds and stocks, portfolio optimization, classical ruin theory, demography and epidemic. 
	"""
	
	cran = "RcmdrPlugin.RiskDemo" 

	version("3.2", md5="26880a9d539baf2d1b4cf083ddfa3238")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
	depends_on("r-demography", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ftsa", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
