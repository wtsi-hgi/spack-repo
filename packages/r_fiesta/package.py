# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFiesta(RPackage):
	"""Forest Inventory Estimation and Analysis

	A research estimation tool for analysts that work with sample-based
    inventory data from the U.S. Department of Agriculture, Forest Service,
    Forest Inventory and Analysis (FIA) Program. 
	"""
	
	homepage = "https://usdaforestservice.github.io/FIESTA/"
	cran = "FIESTA" 

	version("3.6.2", md5="aa043f4e9662ee981cb3e61c492bf6e2")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-fiestautils@1.2.2:", type=("build", "run"))
	depends_on("r-gdalraster", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
