# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobper(RPackage):
	"""Robust Periodogram and Periodicity Detection Methods

	Calculates periodograms based on (robustly) fitting periodic functions to light curves (irregularly observed time series, possibly with measurement accuracies, occurring in astroparticle physics). Three main functions are included: RobPer() calculates the periodogram. Outlying periodogram bars (indicating a period) can be detected with betaCvMfit(). Artificial light curves can be generated using the function tsgen(). For more details see the corresponding article: Thieler, Fried and Rathjens (2016), Journal of Statistical Software 69(9), 1-36, <doi:10.18637/jss.v069.i09>.
	"""
	
	cran = "RobPer" 

	version("1.2.3", md5="639e063901fe7002292afe0171d44fc3")

	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
