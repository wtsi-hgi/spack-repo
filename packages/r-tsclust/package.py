# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsclust(RPackage):
	"""Time Series Clustering Utilities

	A set of measures of dissimilarity between time series to perform time series clustering. Metrics based on raw data, on generating models and on the forecast behavior are implemented. Some additional utilities related to time series clustering are also provided, such as clustering algorithms and cluster evaluation metrics.
	"""
	
	homepage = "http://www.jstatsoft.org/v62/i01/"
	cran = "TSclust" 

	version("1.3.1", md5="5b3011df21696b803c844ab4a2ce6337")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-pdc", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-locpol", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-longitudinaldata", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
