# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTheiar(RPackage):
	"""Download and Manage Data from Theia

	Provides a simple interface to search available data provided by
    Theia (<https://theia.cnes.fr>), download it, and manage it. Data can be downloaded
    based on a search result or from a cart file downloaded from Theia website.
	"""
	
	homepage = "https://github.com/norival/theiaR"
	cran = "theiaR" 

	version("0.4.0", md5="5e3473a9df438efc119d89625060d77e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-askpass@1.1:", type=("build", "run"))
	depends_on("r-httr@1.3:", type=("build", "run"))
	depends_on("r-r6@2.3:", type=("build", "run"))
	depends_on("r-raster@2.6:", type=("build", "run"))
	depends_on("r-xml@3.86:", type=("build", "run"))
