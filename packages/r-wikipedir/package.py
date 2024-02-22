# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWikipedir(RPackage):
	"""A MediaWiki API Wrapper

	A wrapper for the MediaWiki API, aimed particularly at the
    Wikimedia 'production' wikis, such as Wikipedia. It can be used to retrieve
    page text, information about users or the history of pages, and elements of
    the category tree.
	"""
	
	homepage = "https://github.com/Ironholds/WikipediR/"
	cran = "WikipediR" 

	version("1.5.0", md5="784a2f57e0d36a648852540ae4cc3f8a")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
