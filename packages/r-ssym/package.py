# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsym(RPackage):
	"""Fitting Semi-Parametric log-Symmetric Regression Models

	Set of tools to fit a semi-parametric regression model suitable for analysis of data sets in which the response variable is continuous, strictly positive, asymmetric and possibly, censored. Under this setup, both the median and the skewness of the response variable distribution are explicitly modeled by using semi-parametric functions, whose non-parametric components may be approximated by natural cubic splines or P-splines. Supported distributions for the model error include log-normal, log-Student-t, log-power-exponential, log-hyperbolic, log-contaminated-normal, log-slash, Birnbaum-Saunders and Birnbaum-Saunders-t distributions.
	"""
	
	cran = "ssym" 

	version("1.5.8", md5="0536ecf3aa2e91bf28f3aadba3c0a485")

	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-normalp", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
