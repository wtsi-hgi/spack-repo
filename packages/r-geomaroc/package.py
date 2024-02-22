# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomaroc(RPackage):
	"""Easily Visualize Geographic Data of Morocco

	Tools to easily visualize geographic data of Morocco.
    This package interacts with data available through the
    'geomarocdata' package, which is available in a 'drat' 
    repository.   The size of the 'geomarocdata' package is
    approximately 12 MB. 
	"""
	
	homepage = "https://github.com/AmineAndam04/R-geomaroc"
	cran = "geomaroc" 

	version("0.1.1", md5="d57701913bf1ac71edf1be682d485a4b")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
