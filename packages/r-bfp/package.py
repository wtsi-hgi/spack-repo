# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBfp(RPackage):
	"""Bayesian Fractional Polynomials

	Implements the Bayesian paradigm for fractional
 polynomial models under the assumption of normally distributed error terms, see
 Sabanes Bove, D. and Held, L. (2011) <doi:10.1007/s11222-010-9170-7>.
	"""
	
	cran = "bfp" 

	version("0.0-47", md5="a30978e024587c1cda508e1174d04407")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
