# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlshrink(RPackage):
	"""Non-Linear Shrinkage Estimation of Population Eigenvalues and
Covariance Matrices

	Non-linear shrinkage estimation of population eigenvalues and covariance
    matrices, based on publications by Ledoit and Wolf (2004, 2015, 2016).
	"""
	
	cran = "nlshrink" 

	version("1.0.1", md5="5461bd79e7f398ac881d9cebf3b45278")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-nloptr@1.0.4:", type=("build", "run"))
