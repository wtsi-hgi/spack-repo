# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPenmsm(RPackage):
	"""Estimating Regularized Multi-state Models Using L1 Penalties

	Structured fusion Lasso penalized estimation of multi-state models with the penalty applied to absolute effects and absolute effect differences (i.e., effects on transition-type specific hazard rates).
	"""
	
	cran = "penMSM" 

	version("0.99", md5="53c2cff2491d032384fc22f9f447a1d2")

	depends_on("r-rcpp", type=("build", "run"))
