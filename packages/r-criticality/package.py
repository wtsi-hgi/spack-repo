# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCriticality(RPackage):
	"""Modeling Fissile Material Operations in Nuclear Facilities

	A collection of functions for modeling fissile material operations in nuclear facilities,
    based on Zywiec et al (2021) <doi:10.1016/j.ress.2020.107322>.
	"""
	
	cran = "criticality" 

	version("0.9.3", md5="cf0bbaa0c3342abcb37042ba9c9dec81")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
