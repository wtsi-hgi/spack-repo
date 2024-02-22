# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNphazardrate(RPackage):
	"""Nonparametric Hazard Rate Estimation

	Provides functions and examples for histogram, kernel (classical, variable bandwidth and transformations based), discrete and semiparametric hazard rate estimators.
	"""
	
	cran = "NPHazardRate" 

	version("0.1", md5="bfcb8a7b7ed20d91778ce0f405db4e49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
