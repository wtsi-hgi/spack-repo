# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmdb(RPackage):
	"""Access to TMDb API

	Provides an R-interface to the TMDb API (see TMDb API on <https://developers.themoviedb.org/3/getting-started/introduction>). The Movie Database (TMDb) is a popular user editable database for movies and TV shows (see <https://www.themoviedb.org>).
	"""
	
	cran = "TMDb" 

	version("1.1", md5="11a277e7defcc919c8be256d5b4ede15")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-stringi@1.4.6:", type=("build", "run"))
