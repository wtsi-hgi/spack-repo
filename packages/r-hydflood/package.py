# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydflood(RPackage):
	"""Flood Extents and Durations along the Rivers Elbe and Rhine

	Raster based flood modelling internally using 'hyd1d', an R package
    to interpolate 1d water level and gauging data. The package computes flood
    extent and durations through strategies originally developed for 'INFORM',
    an 'ArcGIS'-based hydro-ecological modelling framework. It does not provide
    a full, physical hydraulic modelling algorithm, but a simplified, near real
    time 'GIS' approach for flood extent and duration modelling. Computationally
    demanding annual flood durations have been computed already and data
    products were published by Weber (2022) <doi:10.1594/PANGAEA.948042>.
	"""
	
	homepage = "https://hydflood.bafg.de"
	cran = "hydflood" 

	version("0.5.7", md5="f95df2535114bea2492390973f3b67a0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-hyd1d", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
