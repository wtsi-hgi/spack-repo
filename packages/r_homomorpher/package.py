# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHomomorpher(RPackage):
	"""Homomorphic Computations in R

	Homomorphic computations in R for privacy-preserving applications. Currently only
             the Paillier Scheme is implemented.
	"""
	
	homepage = "http://github.com/bnaras/homomorpheR"
	cran = "homomorpheR" 

	version("0.2-2", md5="28d01219462c22f64cfab127da4dfe59")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-sodium", type=("build", "run"))
