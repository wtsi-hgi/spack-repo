# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNsp(RPackage):
	"""Inference for Multiple Change-Points in Linear Models

	Implementation of Narrowest Significance Pursuit, a general and
    flexible methodology for automatically detecting localised regions in data sequences
    which each must contain a change-point (understood as an abrupt change in the
    parameters of an underlying linear model), at a prescribed global significance level.
    Narrowest Significance Pursuit works with a wide range of distributional assumptions
    on the errors, and yields exact desired finite-sample coverage probabilities,
    regardless of the form or number of the covariates. For details, see P. Fryzlewicz
    (2021) <https://stats.lse.ac.uk/fryzlewicz/nsp/nsp.pdf>.
	"""
	
	cran = "nsp" 

	version("1.0.0", md5="ea1791419e1c40aa8e961eb5a99bb952")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
