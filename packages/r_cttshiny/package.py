# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCttshiny(RPackage):
	"""Classical Test Theory via Shiny

	Interactive shiny application for running classical test theory (item analysis).
	"""
	
	cran = "CTTShiny" 

	version("0.1", md5="e7d8b558f95674d21aa1689a948e1ad1")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-ctt", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
