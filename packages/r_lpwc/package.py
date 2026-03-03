# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpwc(RPackage):
	"""Lag Penalized Weighted Correlation for Time Series Clustering

	Computes a time series distance measure for clustering based on weighted correlation and introduction of lags. The lags capture delayed responses in a time series dataset. The timepoints must be specified. T. Chandereng, A. Gitter (2020) <doi:10.1186/s12859-019-3324-1>.
	"""
	
	homepage = "https://github.com/gitter-lab/LPWC"
	cran = "LPWC" 

	version("1.0.0", md5="bed405fedcc0d8b38f7ff3f3223eebef")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
