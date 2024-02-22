# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArcpy(RPackage):
	"""Interface to 'ArcGIS' 'Python' Modules

	An interface to the 'ArcGIS' 'arcpy' and 'arcgis' 'python' API
    <https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/arcgis-api-for-python.htm>.
    Provides various tools for installing and configuring a 'Conda' environment
    for accessing 'ArcGIS' geoprocessing functions. Helper functions for
    manipulating and converting 'ArcGIS' objects from R are also provided.
	"""
	
	homepage = "https://github.com/mkoohafkan/arcpy"
	cran = "arcpy" 

	version("0.4-0", md5="67b3e329126a868abeda7cbed0bf191c")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-reticulate@1.31:", type=("build", "run"))
