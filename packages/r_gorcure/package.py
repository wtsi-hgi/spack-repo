# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGorcure(RPackage):
	"""Fit Generalized Odds Rate Mixture Cure Model with Interval
Censored Data

	Generalized Odds Rate Mixture Cure (GORMC) model is a flexible model of fitting survival data with a cure fraction, including the Proportional Hazards Mixture Cure (PHMC) model and the Proportional Odds Mixture Cure Model as special cases. This package fit the GORMC model with interval censored data.
	"""
	
	cran = "GORCure" 

	version("2.0", md5="009302b96930b29ca010d1b5c0547106")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-icsurv", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
