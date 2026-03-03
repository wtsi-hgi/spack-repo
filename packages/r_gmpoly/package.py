# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmpoly(RPackage):
	"""Multivariate Polynomials with Rational Coefficients

	Symbolic calculation (addition or multiplication) and evaluation of multivariate polynomials with rational coefficients.
	"""
	
	homepage = "https://github.com/stla/gmpoly"
	cran = "gmpoly" 

	version("1.1.0", md5="9c7fc84b84459ce60f9c03ff69b2a071")

	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-mvp", type=("build", "run"))
	depends_on("r-english", type=("build", "run"))
