# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMswm(RPackage):
	"""Fitting Markov Switching Models

	Estimation, inference and diagnostics for Univariate Autoregressive Markov Switching Models for Linear and Generalized Models. Distributions for the series include gaussian, Poisson, binomial and gamma cases. The EM algorithm is used for estimation (see Perlin (2012) <doi:10.2139/ssrn.1714016>).
	"""
	
	cran = "MSwM" 

	version("1.5", md5="58f89084b33918d81bc70a0068066aae")

	depends_on("r-nlme", type=("build", "run"))
