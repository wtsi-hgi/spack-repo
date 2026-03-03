# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsse(RPackage):
	"""Genotype-Specific Survival Estimation

	We propose a fully efficient sieve maximum likelihood method to estimate genotype-specific distribution of time-to-event outcomes under a nonparametric model. We can handle missing genotypes in pedigrees.  We estimate the time-dependent hazard ratio between two genetic mutation groups using B-splines, while applying nonparametric maximum likelihood estimation to the reference baseline hazard function.  The estimators are calculated via an expectation-maximization algorithm.
	"""
	
	cran = "GSSE" 

	version("0.1", md5="b3484d5989c68097373eb2734e073631")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-iso@0.0.17:", type=("build", "run"))
	depends_on("r-zoo@1.7.12:", type=("build", "run"))
