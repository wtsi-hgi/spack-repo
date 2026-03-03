# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigsplines(RPackage):
	"""Smoothing Splines for Large Samples

	Fits smoothing spline regression models using scalable algorithms designed for large samples. Seven marginal spline types are supported: linear, cubic, different cubic, cubic periodic, cubic thin-plate, ordinal, and nominal. Random effects and parametric effects are also supported. Response can be Gaussian or non-Gaussian: Binomial, Poisson, Gamma, Inverse Gaussian, or Negative Binomial.
	"""
	
	cran = "bigsplines" 

	version("1.1-1", md5="ea7a189e9b0e57b2788d6d3b58f90e4a")

	depends_on("r-quadprog", type=("build", "run"))
