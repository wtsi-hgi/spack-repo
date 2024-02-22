# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHistoslider(RPackage):
	"""A Histogram Slider Input for 'Shiny'

	A histogram slider input binding for use in 'Shiny'. Currently supports creating histograms from numeric, date, and 'date-time' vectors.
	"""
	
	cran = "histoslider" 

	version("0.1.1", md5="7cf77b6e1a9ed623237082d4e945bcab")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
