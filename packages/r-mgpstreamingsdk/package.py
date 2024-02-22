# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgpstreamingsdk(RPackage):
	"""Interact with the Maxar MGP Streaming API

	This grants the functionality of the Maxar Geospatial Platform (MGP) Streaming API. It can search for images using the WFS method. It can Download images using WMS WMTS. It can also Download a full resolution image.
	"""
	
	cran = "mgpStreamingSDK" 

	version("0.2.0", md5="6fb606ef6456d9873f33b63072fffb43")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
