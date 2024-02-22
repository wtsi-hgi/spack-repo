# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIperform(RPackage):
	"""Time Series Performance

	A tool to calculate the performance of a time series in a specific date or period. It is more intended for data analysis in the fields of finance, banking, telecommunications or operational marketing.
	"""
	
	cran = "iperform" 

	version("0.0.3", md5="bdbe3d81e4b6564a8dc05448da101c88")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
