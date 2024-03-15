# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBfw(RPackage):
	"""Bayesian Framework for Computational Modeling

	Derived from the work of Kruschke (2015,
    <ISBN:9780124058880>), the present package aims to provide a framework
    for conducting Bayesian analysis using Markov chain Monte Carlo (MCMC)
    sampling utilizing the Just Another Gibbs Sampler ('JAGS', Plummer,
    2003, <https://mcmc-jags.sourceforge.io>).  The initial version
    includes several modules for conducting Bayesian equivalents of
    chi-squared tests, analysis of variance (ANOVA), multiple
    (hierarchical) regression, softmax regression, and for fitting data
    (e.g., structural equation modeling).
	"""
	
	homepage = "https://github.com/oeysan/bfw/"
	cran = "bfw" 

	version("0.4.2", md5="e14c619aac775ce478eea952d18a356d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-circlize@0.4.4:", type=("build", "run"))
	depends_on("r-coda@0.19.1:", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.7:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-mass@7.3.47:", type=("build", "run"))
	depends_on("r-officer@0.3.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-png@0.1.7:", type=("build", "run"))
	depends_on("r-runjags@2.0.4.2:", type=("build", "run"))
	depends_on("r-rvg@0.1.9:", type=("build", "run"))
	depends_on("r-scales@0.5:", type=("build", "run"))
	depends_on("jags@4.3.0:", type=("build", "link", "run"))
	depends_on("openjdk@1.4:", type=("build", "link", "run"))
