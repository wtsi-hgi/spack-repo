# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGb2(RPackage):
	"""Generalized Beta Distribution of the Second Kind: Properties,
Likelihood, Estimation

	Package GB2 explores the Generalized Beta distribution of the second kind. Density, cumulative distribution function, quantiles and moments of the distributions are given. Functions for the full log-likelihood, the profile log-likelihood and the scores are provided. Formulas for various indicators of inequality and poverty under the GB2 are implemented. The GB2 is fitted by the methods of maximum pseudo-likelihood estimation using the full and profile log-likelihood, and non-linear least squares estimation of the model parameters. Various plots for the visualization and analysis of the results are provided. Variance estimation of the parameters is provided for the method of maximum pseudo-likelihood estimation. A mixture distribution based on the compounding property of the GB2 is presented (denoted as "compound" in the documentation). This mixture distribution is based on the discretization of the distribution of the underlying random scale parameter. The discretization can be left or right tail. Density, cumulative distribution function, moments and quantiles for the mixture distribution are provided. The compound mixture distribution is fitted using the method of maximum pseudo-likelihood estimation. The fit can also incorporate the use of auxiliary information. In this new version of the package, the mixture case is complemented with new functions for variance estimation by linearization and comparative density plots. 
	"""
	
	cran = "GB2" 

	version("2.1.1", md5="09f803e8d1f7af9b53d05f2e63baf388", url="https://cran.r-project.org/src/contrib/GB2_2.1.1.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
	depends_on("r-laeken", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
