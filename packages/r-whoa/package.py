# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhoa(RPackage):
	"""Evaluation of Genotyping Error in Genotype-by-Sequencing Data

	This is a small, lightweight package that lets users investigate the distribution of genotypes in genotype-by-sequencing (GBS) data where they expect (by and large) Hardy-Weinberg equilibrium, in order to assess rates of genotyping errors and the dependence of those rates on read depth.  It implements a Markov chain Monte Carlo (MCMC) sampler using 'Rcpp' to compute a Bayesian estimate of what we call the heterozygote miscall rate for restriction-associated digest (RAD) sequencing data and other types of reduced representation GBS data. It also provides functions to generate plots of expected and observed genotype frequencies. Some background on these topics can be found in a recent paper "Recent advances in conservation and population genomics data analysis" by Hendricks et al. (2018) <doi:10.1111/eva.12659>, and another paper describing the MCMC approach is in preparation with Gordon Luikart and Thierry Gosselin.
	"""
	
	cran = "whoa" 

	version("0.0.2", md5="7ddb658744ab81855a55d6ef35b2bbfe")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-vcfr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
