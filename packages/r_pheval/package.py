# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPheval(RPackage):
	"""Evaluation of the Proportional Hazards Assumption with a
Standardized Score Process

	Provides tools for the evaluation of the goodness of fit and the predictive capacity of the proportional hazards model.
	"""
	
	cran = "PHeval" 

	version("0.5.4", md5="51887779984e1c38818e2de84bd055f5")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
