# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFincal(RPackage):
	"""Time Value of Money, Time Series Analysis and Computational
Finance

	Package for time value of money calculation, time series analysis and computational finance.
	"""
	
	homepage = "http://felixfan.github.io/FinCal/"
	cran = "FinCal" 

	version("0.6.3", md5="a7b5d418191686ce781b6fc9622f82a0")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
