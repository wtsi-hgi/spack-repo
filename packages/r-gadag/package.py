# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGadag(RPackage):
	"""A Genetic Algorithm for Learning Directed Acyclic Graphs

	Sparse large Directed Acyclic Graphs learning with a combination of a convex program and a tailored genetic algorithm (see Champion et al. (2017) <https://hal.archives-ouvertes.fr/hal-01172745v2/document>). 
	"""
	
	cran = "GADAG" 

	version("0.99.0", md5="8cd4c89f3b452034aead53d1300b52d4")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
