# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwn(RPackage):
	"""Taxa Waterbeheer Nederland voor R

	The TWN-list (Taxa Waterbeheer Nederland) is the Dutch standard for naming 
    taxons in Dutch Watermanagement. This package makes it easier to use the 
    TWN-list for ecological analyses. It  consists of two parts. First it makes the 
    TWN-list itself available in R. Second, it has a few functions that make it 
    easy to perform some basic and often recurring tasks for checking and consulting
    taxonomic data from the TWN-list. 
	"""
	
	homepage = "https://redtent.github.io/twn/"
	cran = "twn" 

	version("0.2.4", md5="7e9c67e2d70b11fa07434e27d567d0a5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
