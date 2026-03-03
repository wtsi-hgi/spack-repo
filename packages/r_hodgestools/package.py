# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHodgestools(RPackage):
	"""Common Use Tools for Genomic Analysis

	Built by Hodges lab members for current and future Hodges lab members. Other individuals are welcome to use as well. Provides useful functions that the lab uses everyday to analyze various genomic datasets. Critically, only general use functions are provided; functions specific to a given technique are reserved for a separate package. As the lab grows, we expect to continue adding functions to the package to build on previous lab members code. 
	"""
	
	cran = "HodgesTools" 

	version("1.0.0", md5="d5e786b2cca710d5131af68cea6bdfbf")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-ini", type=("build", "run"))
	depends_on("r-qqman", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-recordlinkage", type=("build", "run"))
