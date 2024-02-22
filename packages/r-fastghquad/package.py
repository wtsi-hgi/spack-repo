# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastghquad(RPackage):
	"""Fast 'Rcpp' Implementation of Gauss-Hermite Quadrature

	Fast, numerically-stable Gauss-Hermite quadrature rules and
    utility functions for adaptive GH quadrature. See Liu, Q. and Pierce, D. A.
    (1994) <doi:10.2307/2337136> for a reference on these methods.
	"""
	
	homepage = "https://github.com/awblocker/fastGHQuad"
	cran = "fastGHQuad" 

	version("1.0.1", md5="168efbf133355e63193f849fb2ca4342")

	depends_on("r-rcpp", type=("build", "run"))
