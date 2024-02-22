# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMuacz(RPackage):
	"""Generate MUAC and BMI z-Scores and Percentiles for Children and
Adolescents

	Generates mid upper arm circumference (MUAC) and body mass index (BMI) 
            for age z-scores and percentiles based on LMS method for children and 
            adolescents up to 19 years that can be used to assess nutritional and health status and
            define risk of adverse health events. 
	"""
	
	cran = "MUACz" 

	version("2.1.0", md5="9fed8363d2aecb4326d0ef25fe2253c7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-epidisplay", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
