# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocits(RPackage):
	"""Test of Stationarity and Localized Autocovariance

	Provides test of second-order stationarity for time
	series (for dyadic and arbitrary-n length data). Provides
	localized autocovariance, with confidence intervals,
	for locally stationary (nonstationary) time series.
	See Nason, G P (2013) "A test for second-order stationarity and
	approximate confidence intervals for localized autocovariance
	for locally stationary time series." Journal of the Royal Statistical
	Society, Series B, 75, 879-904.  <doi:10.1111/rssb.12015>.
	"""
	
	cran = "locits" 

	version("1.7.7", md5="c5d699dce744e94a10bd5c6aadd79f74")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
