# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSunburstr(RPackage):
	"""Sunburst 'Htmlwidget'

	Make interactive 'd3.js' sequence sunburst diagrams in R with the
    convenience and infrastructure of an 'htmlwidget'.
	"""
	
	homepage = "https://github.com/timelyportfolio/sunburstR"
	cran = "sunburstR" 

	version("2.1.8", md5="a6cf1482e0c3dc3eef272f0dd8d113df")

	depends_on("r-d3r@0.6.9:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
