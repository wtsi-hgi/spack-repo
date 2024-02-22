# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsodistrreg(RPackage):
	"""Isotonic Distributional Regression (IDR)

	Distributional regression under stochastic order restrictions for
    numeric and binary response variables and partially ordered covariates. See
    Henzi, Ziegel, Gneiting (2020) <arXiv:1909.03725>.
	"""
	
	homepage = "https://github.com/AlexanderHenzi/isodistrreg"
	cran = "isodistrreg" 

	version("0.1.0", md5="f6433ccd98adbc6759d3247d1c73d8eb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-osqp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
