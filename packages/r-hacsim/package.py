# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHacsim(RPackage):
	"""Iterative Extrapolation of Species' Haplotype Accumulation
Curves for Genetic Diversity Assessment

	Performs iterative extrapolation of species' haplotype accumulation curves using a nonparametric stochastic (Monte Carlo) optimization method for assessment of specimen sampling completeness based on the approach of Phillips et al. (2015) <doi:10.1515/dna-2015-0008>, Phillips et al. (2019) <doi:10.1002/ece3.4757> and Phillips et al. (2020) <doi: 10.7717/peerj-cs.243>. 'HACSim' outputs a number of useful summary statistics of sampling coverage ("Measures of Sampling Closeness"), including an estimate of the likely required sample size (along with desired level confidence intervals) necessary to recover a given number/proportion of observed unique species' haplotypes. Any genomic marker can be targeted to assess likely required specimen sample sizes for genetic diversity assessment. The method is particularly well-suited to assess sampling sufficiency for DNA barcoding initiatives. Users can also simulate their own DNA sequences according to various models of nucleotide substitution. A Shiny app is also available.
	"""
	
	homepage = "<https://github.com/jphill01/HACSim.R>"
	cran = "HACSim" 

	version("1.0.6-1", md5="1b4e61c85662e31a0c3e7645ffe8b8bc")

	depends_on("r-ape@5.3:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-matrixstats@0.56:", type=("build", "run"))
	depends_on("r-pegas@0.13:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
