# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcQpcr(RPackage):
	"""Bayesian Analysis of qRT-PCR Data

	Quantitative RT-PCR data are analyzed using generalized linear mixed models based on lognormal-Poisson error distribution, fitted using MCMC. Control genes are not required but can be incorporated as Bayesian priors or, when template abundances correlate with conditions, as trackers of global effects (common to all genes). The package also implements a lognormal model for higher-abundance data and a "classic" model involving multi-gene normalization on a by-sample basis. Several plotting functions are included to extract and visualize results. The detailed tutorial is available here: <https://matzlab.weebly.com/uploads/7/6/2/2/76229469/mcmc.qpcr.tutorial.v1.2.4.pdf>.
	"""
	
	cran = "MCMC.qpcr" 

	version("1.2.4", md5="d1c18785d523fed7f8572d26cdeb684b")

	depends_on("r-mcmcglmm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
