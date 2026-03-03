# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmsubsets(RPackage):
	"""Exact Variable-Subset Selection in Linear Regression

	Exact and approximation algorithms for variable-subset
  selection in ordinary linear regression models.  Either compute all
  submodels with the lowest residual sum of squares, or determine the
  single-best submodel according to a pre-determined statistical
  criterion.  Hofmann et al. (2020) <doi:10.18637/jss.v093.i03>.
	"""
	
	homepage = "https://github.com/marc-hofmann/lmSubsets.R"
	cran = "lmSubsets" 

	version("0.5-2", md5="cdd9d0496c735a7118751181de6612ba")

	depends_on("r@3.5:", type=("build", "run"))
