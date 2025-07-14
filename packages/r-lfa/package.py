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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/lfa_2.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/lfa/lfa_2.2.0.tar.gz"]

	version("2.8.0", tag="RELEASE_3_21")
	version("2.2.0", sha256="da4a0a2b7dd815a87544c06cb28860fea4601045d308726068f61f210edf3cf7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
