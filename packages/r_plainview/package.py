# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlainview(RPackage):
	"""Plot Raster Images Interactively on a Plain HTML Canvas

	Provides methods for plotting potentially large (raster) images
    interactively on a plain HTML canvas. In contrast to package 'mapview'
    data are plotted without background map, but data can be projected to
    any spatial coordinate reference system.
    Supports plotting of classes 'RasterLayer', 'RasterStack', 'RasterBrick'
    (from package 'raster') as well as 'png' files located on disk. 
    Interactivity includes zooming, panning, and mouse location information. 
    In case of multi-layer 'RasterStacks' or 'RasterBricks', RGB image plots 
    are created (similar to 'raster::plotRGB' - but interactive).
	"""
	
	homepage = "https://r-spatial.github.io/plainview/"
	cran = "plainview" 

	version("0.2.1", md5="cd057cb4d88fb13b2e4ac6c459f2432f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
