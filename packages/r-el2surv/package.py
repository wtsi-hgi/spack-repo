# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REl2surv(RPackage):
	"""Empirical Likelihood (EL) for Comparing Two Survival Functions

	Functions for computing critical values and implementing the one-sided/two-sided EL tests.
	"""
	
	cran = "EL2Surv" 

	version("1.1", md5="acff9fb7c4f3f88e47fb1da5e36f2fea")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
