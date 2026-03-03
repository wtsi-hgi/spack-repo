# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeoperu(RPackage):
	"""Download Spatial Datasets of Peru

	Provides convenient access to the official spatial datasets of Peru as 'sf' objects in R. This package includes a wide range of geospatial data covering various aspects of Peruvian geography, such as: administrative divisions (Source: INEI <https://ide.inei.gob.pe/>), protected natural areas  (Source: GEO ANP - SERNANP <https://geo.sernanp.gob.pe/visorsernanp/>). All datasets are harmonized in terms of attributes, projection, and topology, ensuring consistency and ease of use for spatial analysis and visualization.
	"""
	
	homepage = "https://github.com/PaulESantos/geoperu"
	cran = "geoperu" 

	version("0.0.0.2", md5="5141359867d5e078dcd6db70ffab85dd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
