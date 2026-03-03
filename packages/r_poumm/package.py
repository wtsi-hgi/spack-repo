# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoumm(RPackage):
	"""The Phylogenetic Ornstein-Uhlenbeck Mixed Model

	The Phylogenetic Ornstein-Uhlenbeck Mixed Model (POUMM) allows to 
    estimate the phylogenetic heritability of continuous traits, to test 
    hypotheses of neutral evolution versus stabilizing selection, to quantify 
    the strength of stabilizing selection, to estimate measurement error and to
    make predictions about the evolution of a phenotype and phenotypic variation 
    in a population. The package implements combined maximum likelihood and 
    Bayesian inference of the univariate Phylogenetic Ornstein-Uhlenbeck Mixed 
    Model, fast parallel likelihood calculation, maximum likelihood 
    inference of the genotypic values at the tips, functions for summarizing and
    plotting traces and posterior samples, functions for simulation of a univariate 
    continuous trait evolution model along a phylogenetic tree. So far, the 
    package has been used for estimating the heritability of quantitative traits
    in macroevolutionary and epidemiological studies, see e.g. 
    Bertels et al. (2017) <doi:10.1093/molbev/msx246> and 
    Mitov and Stadler (2018) <doi:10.1093/molbev/msx328>. The algorithm for 
    parallel POUMM likelihood calculation has been published in 
    Mitov and Stadler (2019) <doi:10.1111/2041-210X.13136>.
	"""
	
	homepage = "https://venelin.github.io/POUMM/index.html"
	cran = "POUMM" 

	version("2.1.7", md5="2d661c285ba946fd13071cc5519cfec8")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-data-table@1.13.2:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lamw", type=("build", "run"))
	depends_on("r-adaptmcmc", type=("build", "run"))
