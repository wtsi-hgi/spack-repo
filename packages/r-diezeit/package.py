# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiezeit(RPackage):
	"""R Interface to the ZEIT ONLINE Content API

	A wrapper for the ZEIT ONLINE Content API, available at <http://developer.zeit.de>. 'diezeit' gives access to articles and corresponding metadata from the ZEIT archive and from ZEIT ONLINE. A personal API key is required for usage.
	"""
	
	cran = "diezeit" 

	version("0.1-0", md5="a40c979d5f1caa60274cf19f5c41b76d")

	depends_on("r-brew", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
