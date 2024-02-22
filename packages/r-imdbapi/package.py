# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImdbapi(RPackage):
	"""Get Movie, Television Data from the 'imdb' Database

	Provides API access to the <http://imdbapi.net> which maintains metadata
             about movies, games and television shows through a public API.
	"""
	
	cran = "imdbapi" 

	version("0.1.0", md5="a09ecdfe1f072e2711d48776366ab2ca")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
