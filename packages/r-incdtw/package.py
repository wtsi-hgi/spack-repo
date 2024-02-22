# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIncdtw(RPackage):
	"""Incremental Calculation of Dynamic Time Warping

	The Dynamic Time Warping (DTW) distance measure for time series allows non-linear alignments of time series to match  similar patterns in time series of different lengths and or different speeds. IncDTW is characterized by (1) the incremental calculation of DTW (reduces runtime complexity to a linear level for updating the DTW distance) - especially for life data streams or subsequence matching, (2) the vector based implementation of DTW which is faster because no matrices are allocated (reduces the space complexity from a quadratic to a linear level in the number of observations) - for all runtime intensive DTW computations, (3) the subsequence matching algorithm runDTW, that efficiently finds the k-NN to a query pattern in a long time series, and (4) C++ in the heart. For details about DTW see the original paper "Dynamic programming algorithm optimization for spoken word recognition" by Sakoe and Chiba (1978) <DOI:10.1109/TASSP.1978.1163055>. For details about this package, Dynamic Time Warping and Incremental Dynamic Time Warping please see "IncDTW: An R Package for Incremental Calculation of Dynamic Time Warping" by Leodolter et al. (2021) <doi:10.18637/jss.v099.i09>.
	"""
	
	cran = "IncDTW" 

	version("1.1.4.4", md5="30f87f9d4954b60771fd5a084bd0a062")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
