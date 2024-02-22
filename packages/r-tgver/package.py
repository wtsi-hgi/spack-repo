# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTgver(RPackage):
	"""Turing Geovisualization Engine R package

	Turing Geovisualization Engine R package for geospatial visualization and analysis.
	"""
	
	homepage = "https://github.com/tgve/tgver"
	cran = "tgver" 

	version("0.3.0", md5="28b55277bf9fc08e912d1e4d8f0345c9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plumber", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
