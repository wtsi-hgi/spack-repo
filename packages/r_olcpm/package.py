# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROlcpm(RPackage):
	"""Online Change Point Detection for Matrix-Valued Time Series

	We provide two algorithms for monitoring change points with online matrix-valued time series, under the assumption of a two-way factor structure. The algorithms are based on different calculations of the second moment matrices. One is based on stacking the columns of matrix observations, while another is by a more delicate projected approach. A well-known fact is that, in the presence of a change point, a factor model can be rewritten as a model with a larger number of common factors. In turn, this entails that, in the presence of a change point, the number of spiked eigenvalues in the second moment matrix of the data increases. Based on this, we propose two families of procedures - one based on the fluctuations of partial sums, and one based on extreme value theory - to monitor whether the first non-spiked eigenvalue diverges after a point in time in the monitoring horizon, thereby indicating the presence of a change point. This package also provides some simple functions for detecting and removing outliers, imputing missing entries and testing moments. See more details in He et al. (2021)<arXiv:2112.13479>.
	"""
	
	cran = "OLCPM" 

	version("0.1.1", md5="86a43f332cf6afc86d0fe8a2f72e1452")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
