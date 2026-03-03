# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSns(RPackage):
	"""Stochastic Newton Sampler (SNS)

	Stochastic Newton Sampler (SNS) is a Metropolis-Hastings-based, Markov Chain Monte Carlo sampler for twice differentiable, log-concave probability density functions (PDFs) where the proposal density function is a multivariate Gaussian resulting from a second-order Taylor-series expansion of log-density around the current point. The mean of the Gaussian proposal is the full Newton-Raphson step from the current point. A Boolean flag allows for switching from SNS to Newton-Raphson optimization (by choosing the mean of proposal function as next point). This can be used during burn-in to get close to the mode of the PDF (which is unique due to concavity). For high-dimensional densities, mixing can be improved via 'state space partitioning' strategy, in which SNS is applied to disjoint subsets of state space, wrapped in a Gibbs cycle. Numerical differentiation is available when analytical expressions for gradient and Hessian are not available. Facilities for validation and numerical differentiation of log-density are provided. Note: Formerly available versions of the MfUSampler can be obtained from the archive <https://cran.r-project.org/src/contrib/Archive/MfUSampler/>.
	"""
	
	cran = "sns" 

	version("1.2.2", md5="c287969bf4d564ae2a2339dc68e0064e")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
