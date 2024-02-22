# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcOtu(RPackage):
	"""Bayesian Analysis of Multivariate Counts Data in DNA
Metabarcoding and Ecology

	Poisson-lognormal generalized linear mixed model analysis of multivariate counts data using MCMC, aiming to infer the changes in relative proportions of individual variables. The package was originally designed for sequence-based analysis of microbial communities ("metabarcoding", variables = operational taxonomic units, OTUs), but can be used for other types of multivariate counts, such as in ecological applications (variables = species). The results are summarized and plotted using 'ggplot2' functions. Includes functions to remove sample and variable outliers and reformat counts into normalized log-transformed values for correlation and principal component/coordinate analysis. Walkthrough and examples: http://www.bio.utexas.edu/research/matz_lab/matzlab/Methods_files/walkthroughExample_mcmcOTU_R.txt. 
	"""
	
	cran = "MCMC.OTU" 

	version("1.0.10", md5="a00af8a4245a2c40a665a6230ad83028")

	depends_on("r-mcmcglmm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
