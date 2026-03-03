# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensorevd(RPackage):
	"""A Fast Algorithm to Factorize High-Dimensional Tensor Product
Matrices

	Here we provide tools for the computation and factorization of high-dimensional
	     tensor products that are formed by smaller matrices. The methods are based on
	     properties of Kronecker products (Searle 1982, p. 265, ISBN-10: 0470009616). 
	     We evaluated this methodology by benchmark testing and illustrated its use in 
	     Gaussian Linear Models ('Lopez-Cruz et al., 2024') <doi:10.1093/g3journal/jkae001>.
	"""
	
	cran = "tensorEVD" 

	version("0.1.1", md5="be2cfc227f6cd6b7d881d37e16f4a4e1")

	depends_on("r@3.6:", type=("build", "run"))
