# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResilience(RPackage):
	"""Predictors of Resilience to a Stressor in a Single-Arm Study

	Studies of resilience in older adults employ a single-arm design where everyone experiences the stressor. The simplistic approach of regressing change versus baseline yields biased estimates due to regression-to-the-mean. This package provides a method to correct the bias. It also allows covariates to be included. The method implemented in the package is described in Varadhan, R., Zhu, J., and Bandeen-Roche, K (2023), Biostatistics (To appear).
	"""
	
	cran = "resilience" 

	version("2023.1.1", md5="932da3146515f2f1b38cb77fa69a2518")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nptest", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
