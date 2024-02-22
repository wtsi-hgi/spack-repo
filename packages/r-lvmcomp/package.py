# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLvmcomp(RPackage):
	"""Stochastic EM Algorithms for Latent Variable Models with a
High-Dimensional Latent Space

	Provides stochastic EM algorithms for latent variable models
    with a high-dimensional latent space. So far, we provide functions for confirmatory item
    factor analysis based on the multidimensional two parameter logistic (M2PL) model and the 
    generalized multidimensional partial credit model. These functions scale well for problems
    with many latent traits (e.g., thirty or even more) and are virtually tuning-free.
    The computation is facilitated by multiprocessing 'OpenMP' API.
    For more information, please refer to:
    Zhang, S., Chen, Y., & Liu, Y. (2018). An Improved Stochastic EM Algorithm for Large-scale
    Full-information Item Factor Analysis. British Journal of Mathematical and Statistical
    Psychology. <doi:10.1111/bmsp.12153>.
	"""
	
	homepage = "https://github.com/slzhang-fd/lvmcomp"
	cran = "lvmcomp" 

	version("1.2", md5="7a66a476232b92ca3917c04fd8fc7db6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda@0.19.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
