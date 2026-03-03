# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHypergeomat(RPackage):
	"""Hypergeometric Function of a Matrix Argument

	Evaluates the hypergeometric functions of a matrix argument,
    which appear in random matrix theory. This is an implementation of
    Koev & Edelman's algorithm (2006) <doi:10.1090/S0025-5718-06-01824-2>.
	"""
	
	homepage = "https://github.com/stla/HypergeoMat"
	cran = "HypergeoMat" 

	version("4.0.2", md5="1cd5f9442f21f5384fbe33a2c72f3946")

	depends_on("r-eigenr", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-juliaconnector", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
