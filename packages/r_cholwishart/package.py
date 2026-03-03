# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCholwishart(RPackage):
	"""Cholesky Decomposition of the Wishart Distribution

	Sampling from the Cholesky factorization of a Wishart random 
    variable, sampling from the inverse Wishart distribution, sampling from 
    the Cholesky factorization of an inverse Wishart random variable, sampling
    from the pseudo Wishart distribution, sampling from the generalized
    inverse Wishart distribution, computing densities for the Wishart 
    and inverse Wishart distributions, and computing the multivariate gamma 
    and digamma functions. Provides a header file so the C functions can be
    called directly from other programs.
	"""
	
	homepage = "https://github.com/gzt/CholWishart"
	cran = "CholWishart" 

	version("1.1.2", md5="0cd0c8432450ac68fd4d614cee239f50")

	depends_on("r@3.6:", type=("build", "run"))
