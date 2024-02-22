# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSectorgap(RPackage):
	"""Consistent Economic Trend Cycle Decomposition

	Determining potential output and the output gap - two inherently unobservable variables - is a major challenge for macroeconomists. 'sectorgap' features a flexible modeling and estimation framework for a multivariate Bayesian state space model identifying economic output fluctuations consistent with subsectors of the economy. The proposed model is able to capture various correlations between output and a set of aggregate as well as subsector indicators. Estimation of the latent states and parameters is achieved using a simple Gibbs sampling procedure and various plotting options facilitate the assessment of the results. For details on the methodology and an illustrative example, see Streicher (2024) <https://www.research-collection.ethz.ch/handle/20.500.11850/653682>.
	"""
	
	cran = "sectorgap" 

	version("0.1.0", md5="a4a74693194c06e4aa57a2edf12fd542")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-kfas", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tempdisagg", type=("build", "run"))
