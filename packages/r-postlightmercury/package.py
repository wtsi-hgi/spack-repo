# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPostlightmercury(RPackage):
	"""Parses Web Pages using Postlight Mercury

	This is a wrapper for the Mercury Parser API. The Mercury Parser is 
    a single API endpoint that takes a URL and gives you back the content reliably 
    and easily. 
    With just one API request, Mercury takes any web article and returns 
    only the relevant content — headline, author, body text, relevant images and 
    more — free from any clutter. It’s reliable, easy-to-use and free.
    See the webpage here: <https://mercury.postlight.com/>.
	"""
	
	cran = "postlightmercury" 

	version("1.2", md5="42ae94c1f0612978a353437d91ede481")

	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
