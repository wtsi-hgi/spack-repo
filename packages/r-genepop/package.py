# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenepop(RPackage):
	"""Population Genetic Data Analysis Using Genepop

	Makes the Genepop software available in R. This software implements a mixture of traditional population genetic methods and some more focused developments: it computes exact tests for Hardy-Weinberg equilibrium, for population differentiation and for genotypic disequilibrium among pairs of loci; it computes estimates of F-statistics, null allele frequencies, allele size-based statistics for microsatellites, etc.; and it performs analyses of isolation by distance from pairwise comparisons of individuals or population samples. 
	"""
	
	homepage = "https://www.r-project.org"
	cran = "genepop" 

	version("1.2.2", md5="5fc72670d5c6237dfb373ec79f569bea")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
