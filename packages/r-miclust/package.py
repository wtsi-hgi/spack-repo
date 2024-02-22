# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiclust(RPackage):
	"""Multiple Imputation in Cluster Analysis

	Implementation of a framework for cluster analysis with selection of the
    final number of clusters and an optional variable selection procedure. The package
    is designed to integrate the results of multiple imputed datasets while accounting
    for the uncertainty that the imputations introduce in the final results. In addition,
    the package can also be used for a cluster analysis of the complete cases of a single
    dataset. The package also includes specific methods to summarize and plot the results.
    The methods are described in Basagana et al. (2013) <doi:10.1093/aje/kws289>.
	"""
	
	cran = "miclust" 

	version("1.2.8", md5="e5df1b959a0a50cbbe1708dc62f7551a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-doby", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-flexclust", type=("build", "run"))
	depends_on("r-irr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
