# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSagmm(RPackage):
	"""Clustering via Stochastic Approximation and Gaussian Mixture
Models

	Computes clustering by fitting Gaussian mixture models (GMM) via stochastic approximation following the methods of Nguyen and Jones (2018) <doi:10.1201/9780429446177>. It also provides some test data generation and plotting functionality to assist with this process.
	"""
	
	cran = "SAGMM" 

	version("0.2.4", md5="7715cb9b162b1ed8f0724239cd679666")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mixsim", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-lowmemtkmeans", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
