# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYrmisc(RPackage):
	"""Y&R Miscellaneous R Functions

	Miscellaneous functions for data analysis, portfolio management, graphics, data manipulation, statistical investigation, including descriptive statistics, creating leading and lagging variables, portfolio return analysis, time series difference and percentage change calculation, stacking data for higher efficient analysis.
	"""
	
	cran = "YRmisc" 

	version("0.1.6", md5="215bbd1bf6da19d4e856e07a57c59826")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
