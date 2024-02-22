# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFocusedmds(RPackage):
	"""Focused, Interactive Multidimensional Scaling

	Takes a distance matrix and plots it as an 
    interactive graph. One point is focused at the center of the graph,
    around which all other points are plotted in their exact distances as
    given in the distance matrix. All other non-focus points are plotted 
    as best as possible in relation to one another. Double click on any 
    point to choose a new focus point, and hover over points to see their
    ID labels. If color label categories are given, hover over colors in 
    the legend to highlight only those points and click on colors to 
    highlight multiple groups. For more information on the rationale 
    and mathematical background, as well as an interactive introduction,
    see <https://lea-urpa.github.io/focusedMDS.html>.
	"""
	
	cran = "focusedMDS" 

	version("1.3.3", md5="856a722564b884ffde3c8f23c8412fcc")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
