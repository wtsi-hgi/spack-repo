# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFctbases(RPackage):
	"""Functional Bases

	Easy-to-use, very fast implementation of various functional bases. Easily used together with other packages.
    A functional basis is a collection of basis functions [phi_1, ..., phi_n] that can represent a smooth function, i.e. $f(t) = sum c_k phi_k(t)$.
    First- and second-order derivatives are also included. These are the mathematically correct ones, no approximations applied.
    As of version 1.1, this package includes B-splines, Fourier bases and polynomials.
	"""
	
	homepage = "https://github.com/naolsen/fctbases"
	cran = "fctbases" 

	version("1.1.1", md5="1c33742d4c3836f6537033a4449250ba")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
