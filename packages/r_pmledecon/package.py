# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmledecon(RPackage):
	"""Deconvolution Density Estimation using Penalized MLE

	Given a sample with additive measurement error, the package estimates the deconvolution density - that is, the density of the underlying distribution of the sample without measurement error. The method maximises the log-likelihood of the estimated density, plus a quadratic smoothness penalty. The distribution of the measurement error can be either a known family, or can be estimated from a "pure error" sample. For known error distributions, the package supports Normal, Laplace or Beta distributed error. For unknown error distribution, a pure error sample independent from the data is used.
	"""
	
	cran = "pmledecon" 

	version("0.2.1", md5="f3a8b61e6cae7f0ca34097d99f3fab97")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
