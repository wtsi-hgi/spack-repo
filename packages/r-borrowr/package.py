# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBorrowr(RPackage):
	"""Estimate Causal Effects with Borrowing Between Data Sources

	Estimate population average treatment effects from a primary data source 
  with borrowing from supplemental sources. Causal estimation is done with either a 
  Bayesian linear model or with Bayesian additive regression trees (BART) to adjust 
  for confounding. Borrowing is done with multisource exchangeability models (MEMs). For 
  information on BART, see Chipman, George, & McCulloch (2010) <doi:10.1214/09-AOAS285>. 
  For information on MEMs, see Kaizer, Koopmeiners, & 
  Hobbs (2018) <doi:10.1093/biostatistics/kxx031>.
	"""
	
	cran = "borrowr" 

	version("0.2.0", md5="4eeb3bf157b2177c516e07f549d51a4e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.8:", type=("build", "run"))
	depends_on("r-bart@2.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
