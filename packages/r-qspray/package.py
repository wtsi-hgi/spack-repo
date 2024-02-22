# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQspray(RPackage):
	"""Multivariate Polynomials with Rational Coefficients

	Symbolic calculation and evaluation of multivariate
    polynomials with rational coefficients. This package is strongly
    inspired by the 'spray' package. It also provides a function to 
    compute Gröbner bases (reference <doi:10.1007/978-3-319-16721-3>).
	"""
	
	homepage = "https://github.com/stla/qspray"
	cran = "qspray" 

	version("2.1.1", md5="171aed86fdc667111d4c06840d731186")

	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rationalmatrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ryacas", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("gmp", type=("build", "link", "run"))
	depends_on("mpfr", type=("build", "link", "run"))
