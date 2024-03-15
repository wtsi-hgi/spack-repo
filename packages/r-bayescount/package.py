# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayescount(RPackage):
	"""Power Calculations and Bayesian Analysis of Count Distributions
and FECRT Data using MCMC

	A set of functions to allow analysis of count data (such
        as faecal egg count data) using Bayesian MCMC methods.  Returns
        information on the possible values for mean count, coefficient
        of variation and zero inflation (true prevalence) present in
        the data.  A complete faecal egg count reduction test (FECRT)
        model is implemented, which returns inference on the true
        efficacy of the drug from the pre- and post-treatment data
        provided, using non-parametric bootstrapping as well as using
        Bayesian MCMC.  Functions to perform power analyses for faecal
        egg counts (including FECRT) are also provided.
	"""
	
	homepage = "https://bayescount.sourceforge.net"
	cran = "bayescount" 

	version("0.9.99-9", md5="9e6f4164e8d40abbcba4ead4fee9e3e5")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-runjags@2.0.1:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
