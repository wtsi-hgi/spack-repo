# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdbinseg(RPackage):
	"""Change-Point Analysis of High-Dimensional Time Series via Binary
Segmentation

	Binary segmentation methods for detecting and estimating multiple change-points in the mean or second-order structure of high-dimensional time series as described in Cho and Fryzlewicz (2014) <doi:10.1111/rssb.12079> and Cho (2016) <doi:10.1214/16-EJS1155>.
	"""
	
	cran = "hdbinseg" 

	version("1.0.2", md5="5aa9fe3c1142ff8b114921904070584f")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
