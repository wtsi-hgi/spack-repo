# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrandvec(RPackage):
	"""Generate Random Vectors Whose Components Sum Up to One

	A single method implementing multiple approaches to generate pseudo-random vectors whose components sum up to one (see, e.g., Maziero (2015) <doi:10.1007/s13538-015-0337-8>). The components of such vectors can for example be used for weighting objectives when reducing multi-objective optimisation problems to a single-objective problem in the socalled weighted sum scalarisation approach.
	"""
	
	homepage = "https://jakobbossek.github.io/rrandvec/"
	cran = "rrandvec" 

	version("1.0.0", md5="548ee517c5a27ef6278d1fe53ac3ad4e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
