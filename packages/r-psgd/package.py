# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsgd(RPackage):
	"""Projected Subset Gradient Descent

	Functions to generate ensembles of generalized linear models using
             a greedy projected subset gradient descent algorithm. The sparsity 
             and diversity tuning parameters are selected by cross-validation.
	"""
	
	cran = "PSGD" 

	version("1.0.3", md5="da15bda16f0db049263c6f3078105589")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
