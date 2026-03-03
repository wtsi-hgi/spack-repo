# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasemaps(RPackage):
	"""Accessing Spatial Basemaps in R

	A lightweight package to access spatial basemaps from open sources such as 'OpenStreetMap', 'Carto', 'Mapbox' and others in R.
	"""
	
	cran = "basemaps" 

	version("0.0.6", md5="ab9467450ef426656a741050ed92a27e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-slippymath", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
