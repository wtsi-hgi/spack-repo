# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHardyweinberg(RPackage):
	"""Statistical Tests and Graphics for Hardy-Weinberg Equilibrium

	Contains tools for exploring Hardy-Weinberg equilibrium (Hardy, 1908;  Weinberg, 1908) for bi and multi-allelic genetic marker data. All classical tests (chi-square, exact, likelihood-ratio and permutation tests) with bi-allelic variants are included in the package, as well as functions for power computation and for the simulation of marker data under equilibrium and disequilibrium. Routines for dealing with markers on the X-chromosome are included (Graffelman & Weir, 2016) <doi:10.1038/hdy.2016.20>, including Bayesian procedures. Some exact and permutation procedures also work with multi-allelic variants. Special test procedures that jointly address Hardy-Weinberg equilibrium and equality of allele frequencies in both sexes are supplied, for the bi and multi-allelic case. Functions for testing equilibrium in the presence of missing data by using multiple imputation are also provided. Implements several graphics for exploring the equilibrium status of a large set of bi-allelic markers: ternary plots with acceptance regions, log-ratio plots and Q-Q plots. The functionality of the package is explained in detail in a related JSS paper <doi:10.18637/jss.v064.i03>. 
	"""
	
	homepage = "https://www.r-project.org"
	cran = "HardyWeinberg" 

	version("1.7.7", md5="38f7d848127d74aae9eb88d43387c98a")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
