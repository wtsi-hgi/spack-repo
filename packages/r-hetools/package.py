# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHetools(RPackage):
	"""Homomorphic Encryption Polynomials

	Homomorphic encryption (Brakerski and Vaikuntanathan (2014) <doi:10.1137/120868669>) using Ring Learning with Errors (Lyubashevsky et al. (2012) <https://eprint.iacr.org/2012/230>) is a form of Learning with Errors (Regev (2005) <doi:10.1145/1060590.1060603>) using polynomial rings over finite fields. Functions to generate the required polynomials (using 'polynom'), with various distributions of coefficients are provided. Additionally, functions to generate and take coefficient modulo are provided.
	"""
	
	cran = "HEtools" 

	version("1.0.0", md5="0b46691e762c62ae5527ccc385378bd0")

	depends_on("r-polynom", type=("build", "run"))
