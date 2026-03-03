# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcgor(RPackage):
	"""Fit Generalized Odds Rate Hazards Model with Interval Censored
Data

	Generalized Odds Rate Hazards (GORH) model is a flexible model of fitting survival data, including the Proportional Hazards (PH) model and the Proportional Odds (PO) Model as special cases. This package fit the GORH model with interval censored data.
	"""
	
	cran = "ICGOR" 

	version("2.0", md5="011d53c53b6885a0b982eed9408385e1")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-icsurv", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
