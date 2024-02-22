# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastgasp(RPackage):
	"""Fast and Exact Computation of Gaussian Stochastic Process

	Implements fast and exact computation of Gaussian stochastic process with the Matern kernel using forward filtering and backward smoothing algorithm. It allows for the cases with or without a noise.  See the reference: Mengyang Gu and Yanxun Xu (2017),  <arXiv:1711.11501>.
	"""
	
	cran = "FastGaSP" 

	version("0.5.2", md5="4970b870135e9acb1c464833492c62e3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-robustgasp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
