# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArcpbf(RPackage):
	"""Process ArcGIS Protocol Buffer FeatureCollections

	Fast processing of ArcGIS FeatureCollection protocol buffers in R.
  It is designed to work seamlessly with 'httr2' and integrates with 'sf'. 
	"""
	
	homepage = "https://r.esri.com/arcpbf/"
	cran = "arcpbf"

	version("0.1.0", md5="fe9f542e55b3c468be4b3ec152efc997")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
