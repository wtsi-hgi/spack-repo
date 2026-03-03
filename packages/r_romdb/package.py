# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRomdb(RPackage):
	"""Get 'OMDB' API Multiple Information

	Load multiple movies, series, actors, directors etc from 'OMDB' API. More information in: <http://www.omdbapi.com/> .
	"""
	
	homepage = "https://github.com/AlbertoAlmuinha/ROMDB"
	cran = "ROMDB" 

	version("0.1.0", md5="96adb023bf8212430547c0555feea1ae")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rodbc", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
