# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarkophylo(RPackage):
	"""Markov Chain Models for Phylogenetic Trees

	Allows for fitting of maximum likelihood models using Markov chains
    on phylogenetic trees for analysis of discrete character data. Examples of such
    discrete character data include restriction sites, gene family presence/absence,
    intron presence/absence, and gene family size data. Hypothesis-driven user-
    specified substitution rate matrices can be estimated. Allows for biologically
    realistic models combining constrained substitution rate matrices, site rate
    variation, site partitioning, branch-specific rates, allowing for non-stationary
    prior root probabilities, correcting for sampling bias, etc. See Dang and Golding 
    (2016) <doi:10.1093/bioinformatics/btv541> for more details.
	"""
	
	cran = "markophylo" 

	version("1.0.9", md5="8ca9840feb76f103232734d2cf94e376")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ape@3.2:", type=("build", "run"))
	depends_on("r-numderiv@2012.9.1:", type=("build", "run"))
	depends_on("r-phangorn@1.99.13:", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
