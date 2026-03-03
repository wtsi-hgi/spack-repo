# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparseltseigen(RPackage):
	"""RcppEigen back end for sparse least trimmed squares regression

	Use RcppEigen to fit least trimmed squares
    regression models with an L1 penalty in order to obtain
    sparse models.
	"""
	
	cran = "sparseLTSEigen" 

	version("0.2.0.1", md5="20a0ceae0a6e76b68c7e49c6cd849952")

	depends_on("r-robusthd@0.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
