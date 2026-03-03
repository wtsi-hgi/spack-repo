# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArcokrig(RPackage):
	"""Autoregressive Cokriging Models for Multifidelity Codes

	For emulating multifidelity computer models. The major methods include univariate autoregressive cokriging and multivariate autoregressive cokriging. The autoregressive cokriging methods are implemented for both hierarchically nested design and non-nested design. For hierarchically nested design, the model parameters are estimated via standard optimization algorithms; For non-nested design, the model parameters are estimated via Monte Carlo expectation-maximization (MCEM) algorithms. In both cases, the priors are chosen such that the posterior distributions are proper. Notice that the uniform priors on range parameters in the correlation function lead to improper posteriors. This should be avoided when Bayesian analysis is adopted. The development of objective priors for autoregressive cokriging models can be found in Pulong Ma (2020) <DOI:10.1137/19M1289893>. The development of the multivariate autoregressive cokriging models with possibly non-nested design can be found in Pulong Ma, Georgios Karagiannis, Bledar A Konomi, Taylor G Asher, Gabriel R Toro, and Andrew T Cox (2019) <arXiv:1909.01836>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=ARCokrig"
	cran = "ARCokrig" 

	version("0.1.2", md5="0e6d8d7d787e414d450967fdfe91f835")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
