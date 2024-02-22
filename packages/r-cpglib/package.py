# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpglib(RPackage):
	"""Competing Proximal Gradients Library

	Functions to generate ensembles of generalized linear models using 
             competing proximal gradients. The optimal sparsity and diversity
             tuning parameters are selected via an alternating grid search.
	"""
	
	cran = "CPGLIB" 

	version("1.1.1", md5="034a62a1cf4cfc90b837e6b00f0e56fc")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
