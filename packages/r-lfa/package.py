# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLfa(RPackage):
	"""Logistic Factor Analysis for Categorical Data

	Logistic Factor Analysis is a method for a PCA analogue on Binomial data via estimation of latent structure in the natural parameter.  The main method estimates genetic population structure from genotype data.  There are also methods for estimating individual-specific allele frequencies using the population structure.  Lastly, a structured Hardy-Weinberg equilibrium (HWE) test is developed, which quantifies the goodness of fit of the genotype data to the estimated population structure, via the estimated individual-specific allele frequencies (all of which generalizes traditional HWE tests).
	"""
	
	homepage = "https://github.com/StoreyLab/lfa"
	bioc = "lfa"

	version("2.8.0", commit="bc926127c8b5e55a5610c59049878e670d259d39")
	version("2.2.0", commit="9b4825279a2e2aecb0e1a1baa7cd112ecae9ec67")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
