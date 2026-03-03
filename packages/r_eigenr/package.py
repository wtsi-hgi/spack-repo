# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REigenr(RPackage):
	"""Complex Matrix Algebra with 'Eigen'

	Matrix algebra using the 'Eigen' C++ library: determinant, rank, inverse, pseudo-inverse, kernel and image, QR decomposition, Cholesky decomposition, linear least-squares problems. Also provides matrix functions such as exponential, logarithm, power, sine and cosine. Complex matrices are supported.
	"""
	
	homepage = "https://github.com/stla/EigenR"
	cran = "EigenR" 

	version("1.2.3", md5="9dd3ff5861836383192e6fa3093c6a0e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
