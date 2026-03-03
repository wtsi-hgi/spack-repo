# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsdist(RPackage):
	"""Distance Measures for Time Series Data

	A set of commonly used distance measures and some additional functions which, although initially not designed for this purpose, can be used to measure the dissimilarity between time series. These measures can be used to perform clustering, classification or other data mining tasks which require the definition of a distance measure between time series. U. Mori, A. Mendiburu and J.A. Lozano (2016), <doi:10.32614/RJ-2016-058>.
	"""
	
	cran = "TSdist" 

	version("3.7.1", md5="e553d2b676d86c0ceb8136736d94d37d")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-locpol", type=("build", "run"))
	depends_on("r-longitudinaldata", type=("build", "run"))
	depends_on("r-pdc", type=("build", "run"))
	depends_on("r-tsclust", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
