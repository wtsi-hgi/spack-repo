# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrtshiny(RPackage):
	"""Item Response Theory via Shiny

	Interactive shiny application for running Item Response Theory
    analysis. Provides graphics for characteristic and information curves.
	"""
	
	cran = "IRTShiny" 

	version("1.2", md5="e7344c854acd6a5ada459e576b59075a")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-beeswarm", type=("build", "run"))
	depends_on("r-ctt", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
