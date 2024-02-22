# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROws4r(RPackage):
	"""Interface to OGC Web-Services (OWS)

	Provides an Interface to Web-Services defined as standards by the Open Geospatial Consortium (OGC), including Web Feature Service
 (WFS) for vector data, Web Coverage Service (WCS), Catalogue Service (CSW) for ISO/OGC metadata, Web Processing Service (WPS) for data processes,
 and associated standards such as the common web-service specification (OWS) and OGC Filter Encoding. Partial support is provided for the Web Map 
 Service (WMS). The purpose is to add support for additional OGC service standards such as Web Coverage Processing Service (WCPS), the Sensor 
 Observation Service (SOS), or even new standard services emerging such OGC API or SensorThings.
	"""
	
	homepage = "https://github.com/eblondel/ows4R"
	cran = "ows4R" 

	version("0.3-6", md5="981aed29f96be8613af4edd7cde46077")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-xml@3.96.1.1:", type=("build", "run"))
	depends_on("r-geometa@0.7.1:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
