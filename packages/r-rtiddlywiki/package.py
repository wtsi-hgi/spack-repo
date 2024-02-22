# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtiddlywiki(RPackage):
	"""R Interface for 'TiddlyWiki'

	'TiddlyWiki' is a unique non-linear notebook for capturing, organising and sharing complex information. 'rtiddlywiki' is a R interface of 'TiddlyWiki' <https://tiddlywiki.com> to create new tiddler from Rmarkdown file, and then put into a local 'TiddlyWiki' node.js server if it is available.
	"""
	
	homepage = "https://rtiddlywiki.bangyou.me/"
	cran = "rtiddlywiki" 

	version("0.1.0", md5="9989e06441debbd4a40241a25d002b5f")

	depends_on("r-settings", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
