# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbmsunburst(RPackage):
	"""Generate Personality Insights Sunburst Diagrams

	Generates Personality Insights sunburst diagrams based on
    'IBM Watson' Personality Insights service output.
	"""
	
	homepage = "https://github.com/jumpingrivers/ibmsunburst"
	cran = "ibmsunburst" 

	version("0.1.4", md5="6176245f33155e1217dd5e6e68ace078")
	version("0.1.3", md5="472190cccda07c506b6409867b156b3e")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
