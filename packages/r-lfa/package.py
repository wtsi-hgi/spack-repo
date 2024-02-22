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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/lfa_2.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/lfa/lfa_2.2.0.tar.gz"]

	version("2.2.0", md5="83d3c5671422b432d992834ae675e020")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
