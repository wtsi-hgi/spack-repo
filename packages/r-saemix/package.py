# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaemix(RPackage):
	"""Stochastic Approximation Expectation Maximization (SAEM)
Algorithm

	The 'saemix' package implements the Stochastic Approximation EM algorithm for parameter estimation in (non)linear mixed effects models. The SAEM algorithm (i) computes the maximum likelihood estimator of the population parameters, without any approximation of the model (linearisation, quadrature approximation,...), using the Stochastic Approximation Expectation Maximization (SAEM) algorithm, (ii) provides standard errors for the maximum likelihood estimator (iii) estimates the conditional modes, the conditional means and the conditional standard deviations of the individual parameters, using the Hastings-Metropolis algorithm (see Comets et al. (2017) <doi:10.18637/jss.v080.i03>). Many applications of SAEM in agronomy, animal breeding and PKPD analysis have been published by members of the Monolix group. The full PDF documentation for the package including references about the algorithm and examples can be downloaded on the github of the IAME research institute for 'saemix': <https://github.com/iame-researchCenter/saemix/blob/7638e1b09ccb01cdff173068e01c266e906f76eb/docsaem.pdf>.
	"""
	
	cran = "saemix" 

	version("3.2", md5="293f5ac6931d592d147424766da2fe23")

	depends_on("r-npde@3.2:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
