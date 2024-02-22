# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixak(RPackage):
	"""Multivariate Normal Mixture Models and Mixtures of Generalized
Linear Mixed Models Including Model Based Clustering

	Contains a mixture of statistical methods including the MCMC methods to analyze normal mixtures. Additionally, model based clustering methods are implemented to perform classification based on (multivariate) longitudinal (or otherwise correlated) data. The basis for such clustering is a mixture of multivariate generalized linear mixed models.
	"""
	
	homepage = "https://msekce.karlin.mff.cuni.cz/~komarek/"
	cran = "mixAK" 

	version("5.7", md5="f88a262b9038033dd737427b90fc7889")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-lme4@1:", type=("build", "run"))
	depends_on("r-fastghquad", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
