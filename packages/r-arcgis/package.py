# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArcgis(RPackage):
	"""ArcGIS Location Services Meta-Package

	Provides easy installation and loading of core ArcGIS
    location services packages 'arcgislayers' and 'arcgisutils'. Enabling
    developers to interact with spatial data and services from 'ArcGIS
    Online', 'ArcGIS Enterprise', and 'ArcGIS Platform'. Learn more about
    the 'arcgis' meta-package at <https://r.esri.com/r-bridge-site/>.
	"""
	
	homepage = "https://github.com/R-ArcGIS/arcgis/"
	cran = "arcgis" 

	version("0.1.0", md5="cffd76c43afc2ee8d2b6c503d7138f6a")

	depends_on("r-arcgislayers@0.2:", type=("build", "run"))
	depends_on("r-arcgisutils@0.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-httr2@1:", type=("build", "run"))
