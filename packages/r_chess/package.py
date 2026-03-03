# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChess(RPackage):
	"""Read, Write, Create and Explore Chess Games

	This is an opinionated wrapper around the
    python-chess package. It allows users to read and write PGN files as
    well as create and explore game trees such as the ones seen in chess
    books.
	"""
	
	homepage = "https://github.com/curso-r/chess"
	cran = "chess" 

	version("1.0.1", md5="6de45949875760ab8161ed114798cc68")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
