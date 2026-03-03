# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeasurementprotocol(RPackage):
	"""Send Data from R to the Measurement Protocol

	Send server-side tracking data from R.
  The Measurement Protocol version 2 
  <https://developers.google.com/analytics/devguides/collection/protocol/ga4>
  allows sending HTTP tracking events from R code.
	"""
	
	homepage = "https://code.markedmondson.me/measurementProtocol/"
	cran = "measurementProtocol" 

	version("0.1.1", md5="40b8b311c8c187067414fe53c99dc70d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-rappdirs@0.3.3:", type=("build", "run"))
