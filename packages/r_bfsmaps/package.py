# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBfsmaps(RPackage):
	"""Plot Maps from Switzerland by Swiss Federal Statistical Office

	At the Swiss Federal Statistical Office (SFSO), spatial maps of Switzerland are available free of charge as 'Cartographic bases for small-scale thematic mapping'. This package contains convenience functions to import ESRI (Environmental Systems Research Institute) shape files using the package 'sf' and to plot them easily and quickly without having to worry too much about the technical details.
      It contains utilities to combine multiple areas to one single polygon and to find neighbours for single regions. For any point on a map, a special locator can be used to determine to which municipality, district or canton it belongs.
	"""
	
	homepage = "https://github.com/AndriSignorell/bfsMaps/"
	cran = "bfsMaps" 

	version("1.99.3", md5="3e5deb924a7e58919429f96d9177b81e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
