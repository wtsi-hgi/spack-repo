# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSearcher(RPackage):
	"""Query Search Interfaces

	Provides a search interface to look up terms
    on 'Google', 'Bing', 'DuckDuckGo', 'Startpage', 'Ecosia', 'rseek',
    'Twitter', 'StackOverflow', 'RStudio Community', 'GitHub', and 'BitBucket'.
    Upon searching, a browser window will open with the aforementioned search
    results.
	"""
	
	homepage = "https://github.com/coatless-rpkg/searcher"
	cran = "searcher" 

	version("0.0.7", md5="d4c076d70fb0d693a35a3bd7e7ff348e")

	depends_on("r@3.3:", type=("build", "run"))
