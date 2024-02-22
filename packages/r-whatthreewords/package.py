# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhatthreewords(RPackage):
	"""Work with the 'what3words' API for Easy Location Referencing

	Use the 'what3words' API 
    <https://developer.what3words.com/public-api> to return three words which 
    uniquely identify every 3m x 3m square on Earth. It is also possible to 
    return coordinates from any valid three words location. Supports multiple 
    languages. 
	"""
	
	homepage = "https://davidasmith.github.io/whatthreewords/"
	cran = "whatthreewords" 

	version("0.1.3", md5="9c987fc81d39ac6f20f725a3b2addee4")

	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
