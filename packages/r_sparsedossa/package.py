# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsedossa(RPackage):
	"""Sparse Data Observations for Simulating Synthetic Abundance

	The package is to provide a model based Bayesian method to characterize and simulate microbiome data. sparseDOSSA's model captures the marginal distribution of each microbial feature as a truncated, zero-inflated log-normal distribution, with parameters distributed as a parent log-normal distribution. The model can be effectively fit to reference microbial datasets in order to parameterize their microbes and communities, or to simulate synthetic datasets of similar population structure. Most importantly, it allows users to include both known feature-feature and feature-metadata correlation structures and thus provides a gold standard to enable benchmarking of statistical methods for metagenomic data analysis.
	"""
	
	bioc = "sparseDOSSA" 

	version("1.26.0", commit="2c879d67bf94ab339ad59685c3acf34a35861fc1")

	depends_on("r-optparse", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tmvtnorm@1.4.10:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
