# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistributionsrd(RPackage):
	"""Distribution Fitting and Evaluation

	A library of density, distribution function, quantile function, (bounded) raw moments and random generation for a collection of distributions relevant for the firm size literature. Additionally, the package contains tools to fit these distributions using maximum likelihood and evaluate these distributions based on (i) log-likelihood ratio and (ii) deviations between the empirical and parametrically implied moments of the distributions. We add flexibility by allowing the considered distributions to be combined into piecewise composite or finite mixture distributions, as well as to be used when truncated. See Dewitte (2020) <https://hdl.handle.net/1854/LU-8644700> for a description and application of methods available in this package. 
	"""
	
	cran = "distributionsrd" 

	version("0.0.6", md5="2612c8216071421f6b20cfdb8c634eb9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-modeltools", type=("build", "run"))
