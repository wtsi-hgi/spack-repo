# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfsa(RPackage):
	"""Feasible Solution Algorithm for Finding Best Subsets and
Interactions

	Assists in statistical model building to find optimal and semi-optimal higher order interactions
    and best subsets. Uses the lm(), glm(), and other R functions to fit models generated from a feasible 
    solution algorithm. Discussed in Subset Selection in Regression, A Miller (2002). Applied and explained
    for least median of squares in Hawkins (1993) <doi:10.1016/0167-9473(93)90246-P>. The feasible solution 
    algorithm comes up with model forms of a specific type that can have fixed variables, higher order 
    interactions and their lower order terms.
	"""
	
	cran = "rFSA" 

	version("0.9.6", md5="5527ceb6c705954d487dfa12d009335e")

	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rpref", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
