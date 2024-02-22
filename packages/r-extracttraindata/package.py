# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtracttraindata(RPackage):
	"""Extract Values from Raster

	By using a multispectral image and ESRI shapefile (Point/ Line/ Polygon), a data table will be generated for classification, regression or other processing. The data table will be contained by band wise raster values and shapefile ids (User Defined).
	"""
	
	cran = "ExtractTrainData" 

	version("9.1.6", md5="39df65535c7b8d4e4713814568d339f1")

	depends_on("r-raster", type=("build", "run"))
