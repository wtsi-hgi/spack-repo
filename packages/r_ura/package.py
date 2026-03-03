# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUra(RPackage):
	"""Monitoring Rater Reliability

	Provides researchers with a simple set of diagnostic tools for monitoring the progress and reliability of raters conducting content coding tasks. Goehring (2023) <https://bengoehring.github.io/files/ps-paper-anon-word-ca.docx> argues that supervisors---especially supervisors of small teams---should utilize computational tools to monitor reliability in real time. As such, this package provides easy-to-use functions for calculating inter-rater reliability statistics and measuring the reliability of one coder compared to the rest of the team.
	"""
	
	homepage = "https://github.com/bengoehring/ura"
	cran = "ura" 

	version("1.0.0", md5="09ff910ff9143a8df574fdf7b5120498")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-irr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
