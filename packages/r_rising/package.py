# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRising(RPackage):
	"""High-Dimensional Ising Model Selection

	Fits an Ising model to a binary dataset using L1 regularized
    logistic regression and extended BIC. Also includes a fast lasso logistic
    regression function for high-dimensional problems. Uses the 'libLBFGS'
    optimization library by Naoaki Okazaki.
	"""
	
	cran = "rIsing" 

	version("0.1.0", md5="ebe53a19ce7d6c451d911a9907b0205b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.2.9:", type=("build", "run"))
