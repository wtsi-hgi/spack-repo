# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoncomplyr(RPackage):
	"""Bayesian Analysis of Randomized Experiments with Non-Compliance

	Functions for Bayesian analysis of data from randomized experiments with non-compliance. The functions are based on the models described in Imbens and Rubin (1997) <doi:10.1214/aos/1034276631>. Currently only two types of outcome models are supported: binary outcomes and normally distributed outcomes. Models can be fit with and without the exclusion restriction and/or the strong access monotonicity assumption. Models are fit using the data augmentation algorithm as described in Tanner and Wong (1987) <doi:10.2307/2289457>.
	"""
	
	cran = "noncomplyR" 

	version("1.0", md5="9ecfc003b85e426acb3ef178110cff70")

	depends_on("r-mcmcpack@1.4:", type=("build", "run"))
