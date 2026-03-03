# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcm(RPackage):
	"""Estimating and Testing Intergenerational Social Mobility Effect

	Estimate and test inter-generational social mobility effect on an outcome with cross-sectional or longitudinal data.
	"""
	
	cran = "MCM" 

	version("0.1.7", md5="aedbefb5601e093101507b8f4d282526")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-gee", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-parameters", type=("build", "run"))
