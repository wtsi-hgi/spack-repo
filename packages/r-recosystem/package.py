# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecosystem(RPackage):
	"""Recommender System using Matrix Factorization

	R wrapper of the 'libmf' library
    <https://www.csie.ntu.edu.tw/~cjlin/libmf/> for recommender
    system using matrix factorization. It is typically used to
    approximate an incomplete matrix using the product of two
    matrices in a latent space. Other common names for this task
    include "collaborative filtering", "matrix completion",
    "matrix recovery", etc. High performance multi-core parallel
    computing is supported in this package.
	"""
	
	homepage = "https://github.com/yixuan/recosystem"
	cran = "recosystem" 

	version("0.5.1", md5="0a69550a7c810ee50804b327a706a805")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-float", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
