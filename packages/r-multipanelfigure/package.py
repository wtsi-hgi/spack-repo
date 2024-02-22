# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultipanelfigure(RPackage):
	"""Infrastructure to Assemble Multi-Panel Figures (from Grobs)

	Tools to create a layout for figures made of multiple panels, and
    to fill the panels with base, 'lattice', 'ggplot2' and 'ComplexHeatmap'
    plots, grobs, as well as content from all image formats supported by
    'ImageMagick' (accessed through 'magick').
	"""
	
	cran = "multipanelfigure" 

	version("2.1.5", md5="e80c2af7114635a3cf1d01adf7d0207e")

	depends_on("r-assertive-base@0.0.7:", type=("build", "run"))
	depends_on("r-assertive-files@0.0.2:", type=("build", "run"))
	depends_on("r-assertive-numbers@0.0.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-gridgraphics@0.3.0:", type=("build", "run"))
	depends_on("r-gtable@0.2:", type=("build", "run"))
	depends_on("r-magick@1.9:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-stringi@1.2.3:", type=("build", "run"))
