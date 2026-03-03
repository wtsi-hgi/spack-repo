# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRleafmap(RPackage):
	"""Interactive Maps with R and Leaflet

	Display spatial data with interactive maps powered by the open-
    source JavaScript library 'Leaflet' (see <https://leafletjs.com/>). Maps can be
    rendered in a web browser or displayed in the HTML viewer pane of 'RStudio'.
    This package is designed to be easy to use and can create complex maps with
    vector and raster data, web served map tiles and interface elements.
	"""
	
	homepage = "http://www.francoiskeck.fr/rleafmap/"
	cran = "rleafmap" 

	version("0.2.1", md5="069cd75493f6e92cf1cd95d023440f4c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-knitr@1.5:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
