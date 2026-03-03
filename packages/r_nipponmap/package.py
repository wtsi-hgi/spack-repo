# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNipponmap(RPackage):
	"""Japanese Map Data and Functions

	Digital map data of Japan for choropleth mapping, including a circle cartogram.
	"""
	
	cran = "NipponMap" 

	version("0.2", md5="cef6192c269edc5722292e8fb93d13e0")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
