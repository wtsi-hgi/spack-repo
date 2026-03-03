# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpivottable(RPackage):
	"""Build Powerful Pivot Tables and Dynamically Slice & Dice your
Data

	Build powerful pivot tables (aka Pivot Grid, Pivot Chart, Cross-Tab)
    and dynamically slice & dice / drag 'n' drop your data. 'rpivotTable' is a
    wrapper of 'pivottable', a powerful open-source Pivot Table library implemented
    in 'JavaScript' by Nicolas Kruchten. Aligned to 'pivottable' v2.19.0.
	"""
	
	homepage = "https://github.com/smartinsightsfromdata"
	cran = "rpivotTable" 

	version("0.3.0", md5="e06cf191a720fad261fe9285a94d64c3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.5:", type=("build", "run"))
