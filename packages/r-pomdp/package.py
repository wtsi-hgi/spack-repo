# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPomdp(RPackage):
	"""Infrastructure for Partially Observable Markov Decision
Processes (POMDP)

	Provides the infrastructure to define and analyze the solutions of Partially Observable Markov Decision Process (POMDP) models. Interfaces for various exact and approximate solution algorithms are available including value iteration, point-based value iteration and SARSOP. Smallwood and Sondik (1973) <doi:10.1287/opre.21.5.1071>.
	"""
	
	homepage = "https://github.com/mhahsler/pomdp"
	cran = "pomdp" 

	version("1.1.3", md5="6162774fe52647feb7a51364f760d79c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pomdpsolve@1.0.4:", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
