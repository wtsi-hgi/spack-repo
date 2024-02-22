# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectralr(RPackage):
	"""Obtain and Visualize Spectral Reflectance Data for Earth Surface
Polygons

	Tools for obtaining, processing, and visualizing spectral reflectance data for the user-defined land or water surface classes for visual exploring in which wavelength the classes differ. Input should be a shapefile with polygons of surface classes (it might be different habitat types, crops, vegetation, etc.). The Sentinel-2 L2A satellite mission optical bands pixel data are obtained through the Google Earth Engine service (<https://earthengine.google.com/>) and used as a source of spectral data.
	"""
	
	homepage = "https://github.com/olehprylutskyi/spectralR/"
	cran = "spectralR" 

	version("0.1.3", md5="3a1d65a00f2561b74ae507157fc67269")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rgee@1.1.3:", type=("build", "run"))
	depends_on("r-geojsonio@0.9.4:", type=("build", "run"))
	depends_on("r-sf@1.0.7:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-reshape2@1.4:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
