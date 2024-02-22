# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpicefp(RPackage):
	"""Sparse Method to Identify Joint Effects of Functional Predictors

	A set of functions allowing to implement the 'SpiceFP' approach
  which is iterative. It involves transformation of functional predictors into
  several candidate explanatory matrices (based on contingency tables), to which
  relative edge matrices with contiguity constraints are associated. Generalized
  Fused Lasso regression are performed in order to identify the best candidate
  matrix, the best class intervals and related coefficients at each iteration.
  The approach is stopped when the maximal number of iterations is reached or
  when retained coefficients are zeros. Supplementary functions allow to get
  coefficients of any candidate matrix or mean of coefficients of many candidates.
  The methods in this package are describing in Girault Gnanguenon Guesse, 
  Patrice Loisel, Bénedicte Fontez, Thierry Simonneau, Nadine Hilgert (2021)
  "An exploratory penalized regression to identify combined effects of functional
  variables -Application to agri-environmental issues" 
  <https://hal.archives-ouvertes.fr/hal-03298977>.
	"""
	
	cran = "SpiceFP" 

	version("0.1.2", md5="387b6f3790bc9e2b6e860c6997abafe3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-genlasso", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
