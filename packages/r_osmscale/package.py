# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsmscale(RPackage):
	"""Add a Scale Bar to 'OpenStreetMap' Plots

	Functionality to handle and project lat-long coordinates, easily download background maps
    and add a correct scale bar to 'OpenStreetMap' plots in any map projection.
	"""
	
	homepage = "https://github.com/brry/OSMscale"
	cran = "OSMscale" 

	version("0.5.20", md5="1ca373892345a697d686a936a3a7f822")

	depends_on("r-openstreetmap", type=("build", "run"))
	depends_on("r-berryfunctions@1.15:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
