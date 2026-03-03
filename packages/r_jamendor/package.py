# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJamendor(RPackage):
	"""Access to 'Jamendo' API

	Provides an interface to 'Jamendo' API <https://developer.jamendo.com/v3.0>.
              Pull audio, features and other information for a given 
              'Jamendo' user (including yourself!) or enter an artist's -, album's -, 
              or track's name and retrieve the available information in seconds.
	"""
	
	homepage = "https://github.com/MaxGreil/JamendoR"
	cran = "JamendoR" 

	version("0.1.1", md5="5276df78865f09eba8892f7aa3ba550d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
