# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetexplorer(RPackage):
	"""Network Explorer

	Social network analysis has become an essential tool in the study of complex systems. 'NetExplorer' allows to visualize and explore complex systems. It is based on 'd3js' library that brings 1) Graphical user interface;  2) Circular, linear, multilayer and force Layout; 3) Network live exploration and 4) SVG exportation.
	"""
	
	cran = "NetExplorer" 

	version("0.0.2", md5="7e11473eda250d8c7d783a5540836b64")

	depends_on("r@4:", type=("build", "run"))
