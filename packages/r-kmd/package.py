# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKmd(RPackage):
	"""Kernel Measure of Multi-Sample Dissimilarity

	Implementations of the kernel measure of multi-sample dissimilarity (KMD) between
    several samples using K-nearest neighbor graphs and minimum spanning trees. The KMD 
    measures the dissimilarity between multiple samples, based on the observations from them.
    It converges to the population quantity (depending on the kernel) which is between 0 and 1.
    A small value indicates the multiple samples are from the same distribution, and a large value
    indicates the corresponding distributions are different. The population quantity is 0 if and only
    if all distributions are the same, and 1 if and only if all distributions are mutually singular.
    The package also implements the tests based on KMD for H0: the M distributions are equal
    against H1: not all the distributions are equal. Both permutation test and asymptotic test are
    available. These tests are consistent against all alternatives where at least two samples have
    different distributions. For more details on KMD and the associated tests, see Huang, Z. and
    B. Sen (2022) <arXiv:2210.00634>.
	"""
	
	cran = "KMD" 

	version("0.1.0", md5="79480a4d0901a6066535da24bcd95670")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-mlpack", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
