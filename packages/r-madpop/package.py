# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMadpop(RPackage):
	"""MHC Allele-Based Differencing Between Populations

	Tools for the analysis of population differences
    using the Major Histocompatibility Complex (MHC) genotypes of samples
    having a variable number of alleles (1-4) recorded for each
    individual.  A hierarchical Dirichlet-Multinomial model on the
    genotype counts is used to pool small samples from multiple
    populations for pairwise tests of equality.  Bayesian inference is
    implemented via the 'rstan' package.  Bootstrapped and posterior
    p-values are provided for chi-squared and likelihood ratio tests of
    equal genotype probabilities.
	"""
	
	homepage = "https://github.com/mlysy/MADPop"
	cran = "MADPop" 

	version("1.1.7", md5="95a3939b54099df643d92e065f33ad86")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
