# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfpop(RPackage):
	"""Graph-Constrained Functional Pruning Optimal Partitioning

	Penalized parametric change-point detection by functional pruning dynamic programming algorithm. The successive means are constrained using a graph structure with edges defining the nature of the changes These changes can be unconstrained (type std), up or down constrained (type up and down) or constrained by a minimal size jump (type abs). The type null means that the graph allows us to stay on the same segment. To each edge we can associate some additional properties: a minimal gap size, a penalty, some robust parameters (K,a) for biweight (K) and Huber losses (K and a). The user can also constrain the inferred means to lie between some minimal and maximal values. Data is modeled by a cost with possible use of a robust loss, biweight and Huber (see edge parameters K and a). These costs should have a quadratic, log-linear or a log-log representation. This includes quadratic Gaussian cost (type = 'mean'), log-linear cost (type = 'variance', 'poisson' or 'exp') and log-log cost (type = 'negbin'). More details in the paper published in the Journal of Statistical Software: <doi:10.18637/jss.v106.i06>. 
	"""
	
	cran = "gfpop" 

	version("1.1.1", md5="470dc0265ec27a55ae0702fcce19ceac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
