# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlockcov(RPackage):
	"""Estimation of Large Block Covariance Matrices

	Computation of large covariance matrices having a block structure up to a permutation of their columns and rows 
    from a small number of samples with respect to the dimension of the matrix.
 The method is described in the paper Perrot-Dockès et al. (2019) <arXiv:1806.10093>.
	"""
	
	cran = "BlockCov" 

	version("0.1.1", md5="465fb98734d683ec57c4c52f6f23e5a9")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
