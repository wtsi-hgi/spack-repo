# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTolerance(RPackage):
	"""Statistical Tolerance Intervals and Regions

	Statistical tolerance limits provide the limits between which we can expect to find a specified proportion of a sampled population with a given level of confidence.  This package provides functions for estimating tolerance limits (intervals) for various univariate distributions (binomial, Cauchy, discrete Pareto, exponential, two-parameter exponential, extreme value, hypergeometric, Laplace, logistic, negative binomial, negative hypergeometric, normal, Pareto, Poisson-Lindley, Poisson, uniform, and Zipf-Mandelbrot), Bayesian normal tolerance limits, multivariate normal tolerance regions, nonparametric tolerance intervals, tolerance bands for regression settings (linear regression, nonlinear regression, nonparametric regression, and multivariate regression), and analysis of variance tolerance intervals.  Visualizations are also available for most of these settings.
	"""
	
	cran = "tolerance" 

	version("2.0.0", md5="e2cdbe94d860b8f7234573b728e6bf8d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
