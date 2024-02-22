# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixmixtures(RPackage):
	"""Model-Based Clustering via Matrix-Variate Mixture Models

	Implements finite mixtures of matrix-variate contaminated normal distributions via expectation conditional-maximization algorithm for model-based clustering, as described in Tomarchio et al.(2020) <arXiv:2005.03861>. One key advantage of this model is the ability to automatically detect potential outlying matrices by computing their a posteriori probability of being typical or atypical points. Finite mixtures of matrix-variate t and matrix-variate normal distributions are also implemented by using expectation-maximization algorithms.
	"""
	
	cran = "MatrixMixtures" 

	version("1.0.0", md5="22a0d4ac1f0d24103a26bae1d2d0e119")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
