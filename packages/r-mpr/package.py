# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpr(RPackage):
	"""Multi-Parameter Regression (MPR)

	Fitting Multi-Parameter Regression (MPR) models to right-censored survival data. These are flexible parametric regression models which extend standard models, for example, proportional hazards. See Burke & MacKenzie (2016) <doi:10.1111/biom.12625> and Burke et al (2020) <doi:10.1111/rssc.12398>.
	"""
	
	cran = "mpr" 

	version("1.0.6", md5="686d31d5989527bee2e874bf3979f429")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
