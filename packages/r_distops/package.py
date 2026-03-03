# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistops(RPackage):
	"""Usual Operations for Distance Matrices in R

	It provides the subset operator for dist objects and a function to
    compute medoid(s) that are fully parallelized leveraging the 'RcppParallel'
    package. It also provides functions for package developers to easily
    implement their own parallelized dist() function using a custom 'C++'-based
    distance function.
	"""
	
	homepage = "https://github.com/lmjl-alea/distops"
	cran = "distops" 

	version("0.1.0", md5="2c14d6c7759489319da4488b4b60ff47")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
