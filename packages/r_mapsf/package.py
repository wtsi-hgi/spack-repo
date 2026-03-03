# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapsf(RPackage):
	"""Thematic Cartography

	Create and integrate thematic maps in your workflow. This package
    helps to design various cartographic representations such as proportional
    symbols, choropleth or typology maps. It also offers several functions to
    display layout elements that improve the graphic presentation of maps
    (e.g. scale bar, north arrow, title, labels). 'mapsf' maps 'sf' objects on
    'base' graphics.
	"""
	
	homepage = "https://riatelab.github.io/mapsf/"
	cran = "mapsf" 

	version("0.9.0", md5="d25d0f9ca2ca85f8cadc94b1443bbb22")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-maplegend", type=("build", "run"))
	depends_on("r-s2", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
