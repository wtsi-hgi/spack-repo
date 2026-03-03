# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixsiar(RPackage):
	"""Bayesian Mixing Models in R

	Creates and runs Bayesian mixing models to analyze
    biological tracer data (i.e. stable isotopes, fatty acids), which estimate the
    proportions of source (prey) contributions to a mixture (consumer). 'MixSIAR'
    is not one model, but a framework that allows a user to create a mixing model
    based on their data structure and research questions, via options for fixed/
    random effects, source data types, priors, and error terms. 'MixSIAR' incorporates
    several years of advances since 'MixSIR' and 'SIAR'.
	"""
	
	homepage = "https://github.com/brianstock/MixSIAR"
	cran = "MixSIAR" 

	version("3.1.12", md5="8c8973935c22343d0f2d1aeca22802ca")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-r2jags@0.5.7:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1:", type=("build", "run"))
	depends_on("r-reshape@0.8.7:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-lattice@0.20.35:", type=("build", "run"))
	depends_on("r-mcmcpack@1.4.2:", type=("build", "run"))
	depends_on("r-ggmcmc@1.1:", type=("build", "run"))
	depends_on("r-coda@0.19.1:", type=("build", "run"))
	depends_on("r-loo@2:", type=("build", "run"))
	depends_on("r-bayesplot@1.4:", type=("build", "run"))
	depends_on("r-splancs@2.1.40:", type=("build", "run"))
	depends_on("jags@4.3:", type=("build", "link", "run"))
