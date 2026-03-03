# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplesize4surveys(RPackage):
	"""Sample Size Calculations for Complex Surveys

	Computes the required sample size for estimation of totals, means
    and proportions under complex sampling designs.
	"""
	
	cran = "samplesize4surveys" 

	version("4.1.1", md5="2a75f2cca234c0a37a95efe0b0db8be2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-teachingsampling", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
