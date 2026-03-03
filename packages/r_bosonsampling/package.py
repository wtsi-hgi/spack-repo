# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBosonsampling(RPackage):
	"""Classical Boson Sampling

	Classical Boson Sampling using the algorithm of
 Clifford and Clifford (2017) <arXiv:1706.01260>. Also provides functions for
 generating random unitary matrices, evaluation of matrix permanents (both
 real and complex) and evaluation of complex permanent minors.
	"""
	
	cran = "BosonSampling" 

	version("0.1.5", md5="baf41afa36d6a0d60c7dfc33dc6172b8")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
