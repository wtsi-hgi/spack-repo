# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsrepr(RPackage):
	"""Time Series Representations

	Methods for representations (i.e. dimensionality reduction, preprocessing, feature extraction) of time series to help more accurate and effective time series data mining.
    Non-data adaptive, data adaptive, model-based and data dictated (clipped) representation methods are implemented. Also various normalisation methods (min-max, z-score, Box-Cox, Yeo-Johnson),
    and forecasting accuracy measures are implemented.
	"""
	
	homepage = "https://petolau.github.io/package/"
	cran = "TSrepr" 

	version("1.1.0", md5="99e5cbe4a4d3b77cdde7b8e2bb7d954c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-wavelets", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-dtt", type=("build", "run"))
