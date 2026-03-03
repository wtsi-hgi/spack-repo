# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiesmuschel(RPackage):
	"""Mixed Integer Evolution Strategies

	Evolutionary black box optimization algorithms building on the
  'bbotk' package. 'miesmuschel' offers both ready-to-use optimization
  algorithms, as well as their fundamental building blocks that can be used to
  manually construct specialized optimization loops. The Mixed Integer Evolution
  Strategies as described by Li et al. (2013) <doi:10.1162/EVCO_a_00059> can be
  implemented, as well as the multi-objective optimization algorithms NSGA-II
  by Deb, Pratap, Agarwal, and Meyarivan (2002) <doi:10.1109/4235.996017>.
	"""
	
	homepage = "https://github.com/mlr-org/miesmuschel"
	cran = "miesmuschel" 

	version("0.0.3", md5="96d4d6147f4b82bc2e464a18e8303d73")

	depends_on("r-paradox@0.7.1:", type=("build", "run"))
	depends_on("r-mlr3misc@0.5:", type=("build", "run"))
	depends_on("r-checkmate@1.9:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-bbotk@0.3.0.900:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
