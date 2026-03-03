# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdshiny(RPackage):
	"""'Probability Distribution Shiny'

	Interactive shiny application for working with Probability Distributions. Calculations and  Graphs are provided.
	"""
	
	cran = "PDShiny" 

	version("0.1.0", md5="5f35b82cd661b93b22fe0dc0ebe8b4ef")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
