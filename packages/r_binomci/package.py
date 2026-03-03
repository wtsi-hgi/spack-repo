# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinomci(RPackage):
	"""Confidence Intervals for a Binomial Proportion

	Twelve confidence intervals for one binomial proportion or a vector of binomial proportions are computed. The confidence intervals are: Jeffreys,  Wald, Wald corrected, Wald, Blyth and Still,  Agresti and Coull, Wilson, Score, Score corrected, Wald logit, Wald logit corrected, Arcsine and Exact binomial. References include, among others: Vollset, S. E. (1993). "Confidence intervals for a binomial proportion". Statistics in Medicine, 12(9): 809-824. <doi:10.1002/sim.4780120902>. 
	"""
	
	cran = "binomCI" 

	version("1.1", md5="fbe297a702fd6d64ddb6d5655d61e2db")

	depends_on("r@4.3:", type=("build", "run"))
