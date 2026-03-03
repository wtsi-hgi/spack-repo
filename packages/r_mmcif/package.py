# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmcif(RPackage):
	"""Mixed Multivariate Cumulative Incidence Functions

	Fits the mixed cumulative incidence functions model suggested by 
    <doi:10.1093/biostatistics/kxx072> which decomposes within cluster 
    dependence of risk and timing. The estimation method supports computation in 
    parallel using a shared memory C++ implementation. A sandwich estimator of the 
    covariance matrix is available. Natural cubic splines are used to provide a 
    flexible model for the cumulative incidence functions.
	"""
	
	homepage = "https://github.com/boennecd/mmcif"
	cran = "mmcif" 

	version("0.1.1", md5="b97d80b3409b2851b1e0aa18f52b5f4f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-psqn", type=("build", "run"))
