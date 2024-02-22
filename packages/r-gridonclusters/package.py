# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGridonclusters(RPackage):
	"""Cluster-Preserving Multivariate Joint Grid Discretization

	Discretize multivariate continuous data using a grid
 that captures the joint distribution via preserving clusters in
 the original data (Wang et al. 2020) <doi:10.1145/3388440.3412415>.
 Joint grid discretization is applicable as a data transformation step
 to prepare data for model-free inference of association, function, or
 causality.
	"""
	
	cran = "GridOnClusters" 

	version("0.1.0", md5="abba546aa87140ad4e641dcb565517e9")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ckmeans-1d-dp", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fossil", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
