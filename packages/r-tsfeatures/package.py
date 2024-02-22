# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsfeatures(RPackage):
	"""Time Series Feature Extraction

	Methods for extracting various features from time series data. The features provided are those from Hyndman, Wang and Laptev (2013) <doi:10.1109/ICDMW.2015.104>, Kang, Hyndman and Smith-Miles (2017) <doi:10.1016/j.ijforecast.2016.09.004> and from Fulcher, Little and Jones (2013) <doi:10.1098/rsif.2013.0048>. Features include spectral entropy, autocorrelations, measures of the strength of seasonality and trend, and so on. Users can also define their own feature functions.
	"""
	
	homepage = "https://pkg.robjhyndman.com/tsfeatures/"
	cran = "tsfeatures" 

	version("1.1.1", md5="275dc66ba646f24c9e8a44d4eb0818ff")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-forecast@8.3:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpproll@0.2.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
