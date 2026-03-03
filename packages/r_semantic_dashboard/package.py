# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemanticDashboard(RPackage):
	"""Dashboard with Fomantic UI Support for Shiny

	It offers functions for creating dashboard with Fomantic UI. 
	"""
	
	cran = "semantic.dashboard" 

	version("0.2.1", md5="27b6aed8d1b179700004b6301a67dfab")

	depends_on("r-shiny@0.12.1:", type=("build", "run"))
	depends_on("r-shiny-semantic@0.3.3:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
