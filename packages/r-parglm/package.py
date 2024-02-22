# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParglm(RPackage):
	"""Parallel GLM

	Provides a parallel estimation method for generalized 
  linear models without compiling with a multithreaded LAPACK or BLAS.
	"""
	
	homepage = "https://github.com/boennecd/parglm"
	cran = "parglm" 

	version("0.1.7", md5="fbc408df75ac84d26e415d150d978182")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
