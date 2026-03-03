# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPressure(RPackage):
	"""Imports, Processes, and Visualizes Biomechanical Pressure Data

	Allows biomechanical pressure data from a range of systems to be imported and processed in a reproducible manner. Automatic and manual tools are included to let the user define regions (masks) to be analyzed. Also includes functions for visualizing and animating pressure data. Example methods are described in Shi et al., (2022) <doi:10.1038/s41598-022-19814-0>, Lee et al., (2014) <doi:10.1186/1757-1146-7-18>, van der Zward et al., (2014) <doi:10.1186/1757-1146-7-20>, and Najafi et al., (2010) <doi:10.1016/j.gaitpost.2009.09.003>.
	"""
	
	cran = "pressuRe" 

	version("0.2.3", md5="e8b4da5b49b2f4d423096e1788f771f8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gdistance", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
