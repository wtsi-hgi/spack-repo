# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdcd(RPackage):
	"""High-Dimensional Changepoint Detection

	Efficient implementations of the following multiple changepoint detection algorithms: Efficient Sparsity Adaptive Change-point estimator by Moen, Glad and Tveten (2023) <arXiv:2306.04702> , Informative Sparse Projection for Estimating Changepoints by Wang and Samworth (2017) <doi:10.1111/rssb.12243>, and the method of Pilliat et al (2023) <doi:10.1214/23-EJS2126>.
	"""
	
	cran = "HDCD" 

	version("1.0", md5="0b230acb0a98df61b7986d5776af0234")

	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
