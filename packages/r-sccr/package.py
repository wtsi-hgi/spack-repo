# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSccr(RPackage):
	"""The Self-Consistent, Competing Risks (SC-CR) Algorithms

	The SC-SR Algorithm is used to calculate fully non-parametric and self-consistent estimators of the cause-specific failure probabilities in the presence of interval-censoring and possible making of the failure cause in a competing risks environment. In the version 2.0 the function creating the probability matrix from double-censored data is added.
	"""
	
	cran = "sccr" 

	version("2.1", md5="5692e74fed5b52b16657633a4cb98b4b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
