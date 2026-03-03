# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsoutliers(RPackage):
	"""Detection of Outliers in Time Series

	Detection of outliers in time series following the 
    Chen and Liu (1993) <DOI:10.2307/2290724> procedure. 
    Innovational outliers, additive outliers, level shifts, 
    temporary changes and seasonal level shifts are considered.
	"""
	
	homepage = "https://jalobe.com"
	cran = "tsoutliers" 

	version("0.6-10", md5="245b8676918ff032809870b38384aa83")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
