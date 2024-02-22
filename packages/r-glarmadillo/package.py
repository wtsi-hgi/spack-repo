# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlarmadillo(RPackage):
	"""Solve the Graphical Lasso Problem with 'Armadillo'

	Efficiently implements the Graphical Lasso algorithm,
            utilizing the 'Armadillo' 'C++' library for rapid computation. This algorithm 
            introduces an L1 penalty to derive sparse inverse covariance matrices from 
            observations of multivariate normal distributions. Features include the 
            generation of random and structured sparse covariance matrices, beneficial 
            for simulations, statistical method testing, and educational purposes in 
            graphical modeling. A unique function for regularization parameter selection 
            based on predefined sparsity levels is also offered, catering to users with
            specific sparsity requirements in their models. The methodology for sparse 
            inverse covariance estimation implemented in this package is based on the 
            work of Friedman, Hastie, and Tibshirani (2008) <doi:10.1093/biostatistics/kxm045>.
	"""
	
	cran = "Glarmadillo" 

	version("1.1.1", md5="f203f93bcd99e3f227d132e7d4c94663")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
