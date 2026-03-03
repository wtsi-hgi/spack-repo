# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWikitools(RPackage):
	"""Tools for Wikidata and Wikipedia

	A set of wrappers intended to check, read and download information from the Wikimedia sources. It is specifically created to work with names of celebrities, in which case their information and statistics can be downloaded. Additionally, it also builds links and snippets to use in combination with the function gallery() in netCoin package.
	"""
	
	cran = "wikiTools" 

	version("0.0.6", md5="86c2f0aad48341138934908fbad6991f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-wikidataqueryservicer@1:", type=("build", "run"))
	depends_on("r-wikidatar@1.4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ratelimitr", type=("build", "run"))
