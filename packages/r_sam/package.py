# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSam(RPackage):
	"""Sparse Additive Modelling

	Computationally efficient tools for high dimensional predictive
        modeling (regression and classification). SAM is short for sparse 
        additive modeling, and adopts the computationally efficient basis 
        spline technique. We solve  the optimization problems by various 
        computational algorithms including the block coordinate descent 
        algorithm, fast iterative soft-thresholding algorithm, and newton method. 
        The computation is further accelerated by warm-start and active-set tricks.
	"""
	
	cran = "SAM" 

	version("1.1.3", md5="cef7b25ff772f2daace3b718fbef04da")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
