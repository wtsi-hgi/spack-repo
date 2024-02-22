# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaussquad(RPackage):
	"""Collection of Functions for Gaussian Quadrature

	A collection of functions to perform Gaussian quadrature
        with different weight functions corresponding to the orthogonal
        polynomials in package orthopolynom.  Examples verify the
        orthogonality and inner products of the polynomials.
	"""
	
	cran = "gaussquad" 

	version("1.0-3", md5="6c87c289baf69f725c2abb015fc77b58")

	depends_on("r@2.0.1:", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
