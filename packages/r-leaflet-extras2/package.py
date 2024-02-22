# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeafletExtras2(RPackage):
	"""Extra Functionality for 'leaflet' Package

	Several 'leaflet' plugins are integrated, which are available as extension to the 'leaflet' package.
	"""
	
	homepage = "https://trafficonese.github.io/leaflet.extras2/"
	cran = "leaflet.extras2" 

	version("1.2.2", md5="8aaed666b60f626f6ce17c3be56d5245", url="https://cran.r-project.org/src/contrib/leaflet.extras2_1.2.2.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-leaflet@2:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
