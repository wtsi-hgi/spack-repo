# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIetd(RPackage):
	"""Inter-Event Time Definition

	Computes characteristics of independent rainfall events (duration, total rainfall depth, and intensity) 
  extracted from a sub-daily rainfall time series based on the inter-event time definition (IETD) method. To have a 
  reference value of IETD, it also analyzes/computes IETD values through three methods: autocorrelation analysis, the 
  average annual number of events analysis, and coefficient of variation analysis. Ideal for analyzing the sensitivity 
  of IETD to characteristics of independent rainfall events.
  Adams B, Papa F (2000) <ISBN: 978-0-471-33217-6>.
  Joo J et al. (2014) <doi:10.3390/w6010045>.
  Restrepo-Posada P, Eagleson P (1982) <doi:10.1016/0022-1694(82)90136-6>.
	"""
	
	cran = "IETD" 

	version("1.0.0", md5="b6c01d26d203dce9e46c1685c0d1c44e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
