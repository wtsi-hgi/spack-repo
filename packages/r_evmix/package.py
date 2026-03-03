# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvmix(RPackage):
	"""Extreme Value Mixture Modelling, Threshold Estimation and
Boundary Corrected Kernel Density Estimation

	The usual distribution functions, maximum likelihood inference and
    model diagnostics for univariate stationary extreme value mixture models
    are provided. Kernel density estimation including various boundary
    corrected kernel density estimation methods and a wide choice of kernels,
    with cross-validation likelihood based bandwidth estimator.
    Reasonable consistency with the base functions in the 'evd' package is
    provided, so that users can safely interchange most code.
	"""
	
	homepage = "http://www.math.canterbury.ac.nz/~c.scarrott/evmix"
	cran = "evmix" 

	version("2.12", md5="20660d1aedd961d7c1224679ab25328c")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
