# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApci(RPackage):
	"""A New Age-Period-Cohort Model for Describing and Investigating
Inter-Cohort Differences and Life Course Dynamics

	It implemented Age-Period-Interaction Model (APC-I Model) proposed in the paper of Liying Luo and James S. Hodges in 2019. A new age-period-cohort model for describing and investigating inter-cohort differences and life course dynamics.
	"""
	
	cran = "APCI" 

	version("1.0.7", md5="283665689923b8e424a20f630a9c8e76")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-gee", type=("build", "run"))
