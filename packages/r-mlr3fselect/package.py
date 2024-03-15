# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3fselect(RPackage):
	"""Feature Selection for 'mlr3'

	Feature selection package of the 'mlr3' ecosystem. It selects
    the optimal feature set for any 'mlr3' learner. The package works with
    several optimization algorithms e.g. Random Search, Recursive Feature
    Elimination, and Genetic Search. Moreover, it can automatically
    optimize learners and estimate the performance of optimized feature
    sets with nested resampling.
	"""
	
	homepage = "https://mlr3fselect.mlr-org.com"
	cran = "mlr3fselect" 

	version("0.12.0", md5="8aeba638268cbe1f62bb9114ec78929e")

	depends_on("r-mlr3@0.12:", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-bbotk@0.7.2:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-mlr3misc@0.9.4:", type=("build", "run"))
	depends_on("r-paradox@0.7:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
