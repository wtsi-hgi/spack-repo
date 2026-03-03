# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpackedbar(RPackage):
	"""Packed Bar Charts with 'plotly'

	Packed bar charts are a variation of treemaps for visualizing skewed data.  The concept was introduced by Xan Gregg at 'JMP'.
	"""
	
	homepage = "https://github.com/AdamSpannbauer/rPackedBar"
	cran = "rPackedBar" 

	version("0.2.2", md5="186546152ca33ecb768da36bf52cb2f9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
