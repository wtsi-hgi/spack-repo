# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdamatch(RPackage):
	"""Selection of Statistically Similar Research Groups

	Select statistically similar research groups by backward selection using various robust algorithms, including a heuristic based on linear discriminant analysis, multiple heuristics based on the test statistic, and parallelized exhaustive search.
	"""
	
	cran = "ldamatch" 

	version("1.0.2", md5="d5626ba8f81b2fe0a4a654c2301363be")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-iterpc", type=("build", "run"))
	depends_on("r-ksamples", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
