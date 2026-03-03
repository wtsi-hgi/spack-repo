# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDifshiny(RPackage):
	"""Differential Item Functioning via Shiny Application

	Differential Item Functioning (DIF) Analysis with shiny application interfaces. You can run the functions in this package without any arguments and perform your DIF analysis using user-friendly interfaces.
	"""
	
	cran = "DIFshiny" 

	version("0.1.0", md5="1e0ca0b0a0fa354f661677a0bd4aff5e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-difr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
