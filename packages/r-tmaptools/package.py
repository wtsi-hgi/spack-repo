# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmaptools(RPackage):
	"""Thematic Map Tools

	Set of tools for reading and processing spatial data. The aim is to supply the workflow to create thematic maps. This package also facilitates 'tmap', the package for visualizing thematic maps.
	"""
	
	homepage = "https://github.com/mtennekes/tmaptools"
	cran = "tmaptools" 

	version("3.1-1", md5="25d2726a3032f6bb3d6ec283c5d5c469")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf@0.9.2:", type=("build", "run"))
	depends_on("r-lwgeom@0.1.4:", type=("build", "run"))
	depends_on("r-stars@0.4.1:", type=("build", "run"))
	depends_on("r-units@0.6.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-dichromat", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
