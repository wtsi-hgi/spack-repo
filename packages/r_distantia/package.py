# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistantia(RPackage):
	"""Assessing Dissimilarity Between Multivariate Time Series

	Provides tools to assess the dissimilarity between multivariate time-series. It is based on the psi measure described  by Birks and Gordon (1985 <doi:10.1002/jqs.3390020110>), which computes dissimilarity between irregular time-series constrained by sample order. However, in this package the original idea has been extended to work with any kind of multivariate time-series, no matter whether they are regular, irregular, aligned or unaligned. Furthermore, the package allows to assess the significance of dissimilarity values by applying a restricted permutation test, allows to measure the contribution of individual variables to dissimilarity, and offers tools to transfer attributes (generally time or age, but other are possible) between sequences based on the similarity of their samples.
	"""
	
	homepage = "https://blasbenito.github.io/distantia/"
	cran = "distantia" 

	version("1.0.2", md5="3d36d8d4e6a085786882ed755548528a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-arrangements", type=("build", "run"))
