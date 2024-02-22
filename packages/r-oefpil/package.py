# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROefpil(RPackage):
	"""Optimal Estimation of Function Parameters by Iterated
Linearization

	Package for estimating the parameters of a nonlinear function using iterated linearization via Taylor series.  Method is based on  Kubáček (2000) ISBN: 80-244-0093-6. The algorithm is a generalization of the procedure given in Köning, R., Wimmer, G.
             and Witkovský, V. (2014) <doi:10.1088/0957-0233/25/11/115001>.
	"""
	
	cran = "OEFPIL" 

	version("0.1.1", md5="5c752a91a8941f960f2d545f904d0ace")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
