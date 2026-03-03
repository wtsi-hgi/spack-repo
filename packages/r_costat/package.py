# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCostat(RPackage):
	"""Time Series Costationarity Determination

	Contains functions that can determine whether a time series
	is second-order stationary or not (and hence evidence for
	locally stationarity). Given two non-stationary series (i.e.
	locally stationary series) this package can then discover
	time-varying linear combinations that are second-order stationary.
	Cardinali, A. and Nason, G.P. (2013)
	<doi:10.18637/jss.v055.i01>.
	"""
	
	cran = "costat" 

	version("2.4.1", md5="5e6239eaa6f89ad4d09859b348477a36")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-wavethresh@4.6.1:", type=("build", "run"))
