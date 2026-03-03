# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPersomicsarray(RPackage):
	"""Automated Persomics Array Image Extraction

	Automated identification of printed array positions from high content 
    microscopy images and the export of those positions as individual images 
    written to output as multi-layered tiff files.
	"""
	
	cran = "PersomicsArray" 

	version("1.0", md5="b2452e8e91f7d2a56cd7927c847e8576")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
