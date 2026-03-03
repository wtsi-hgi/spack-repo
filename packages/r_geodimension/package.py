# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeodimension(RPackage):
	"""Definition of Geographic Dimensions

	The geographic dimension plays a fundamental role in
    multidimensional systems. To define a geographic dimension in a star
    schema, we need a table with attributes corresponding to the levels of
    the dimension. Additionally, we will also need one or more geographic
    layers to represent the data using this dimension. The goal of this
    package is to support the definition of geographic dimensions from
    layers of geographic information related to each other. It makes it
    easy to define relationships between layers and obtain the necessary
    data from them.
	"""
	
	homepage = "https://josesamos.github.io/geodimension/"
	cran = "geodimension" 

	version("2.0.0", md5="354e8307e9c08a62bd35a8175962b604")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
