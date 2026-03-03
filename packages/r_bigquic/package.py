# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigquic(RPackage):
	"""Big Quadratic Inverse Covariance Estimation

	Use Newton's method, coordinate descent, and METIS clustering
    to solve the L1 regularized Gaussian MLE inverse covariance
    matrix estimation problem.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "BigQuic" 

	version("1.1-13", md5="a0c040c11b47af28a502d172f3e13e0e")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-scalreg", type=("build", "run"))
