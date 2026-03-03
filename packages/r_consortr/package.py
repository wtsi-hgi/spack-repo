# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsortr(RPackage):
	"""Interactive Consort Flow Diagrams

	Shiny app for creating interactive consort flow diagrams and other types of flow diagrams, see Moher, Schulz and Altman (2001) <doi:10.1016/S0140-6736(00)04337-3>.
	"""
	
	cran = "consortr" 

	version("0.9.1", md5="e1b0d8975b707b1543e8a08ec821abf2")

	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
