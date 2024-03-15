# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmixclust(RPackage):
	"""Time Series Clustering of Gene Expression with Gaussian Mixed-Effects
	Models and Smoothing Splines.

	Implementation of a clustering method for time series gene expression
	data based on mixed-effects models with Gaussian variables and non-
	parametric cubic splines estimation. The method can robustly account for
	the high levels of noise present in typical gene expression time series
	datasets."""

	bioc = "TMixClust"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TMixClust_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TMixClust/TMixClust_1.24.0.tar.gz"]

	version("1.24.0", md5="3e0e6852e806722f305ed45332c23179")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-gss", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-flexclust", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-spem", type=("build", "run"))
