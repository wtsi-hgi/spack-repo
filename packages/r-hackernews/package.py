# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHackernews(RPackage):
	"""Wrapper for the 'Official Hacker News' API

	Use the <https://hacker-news.firebaseio.com/v0/> API through R. Retrieve
    posts, articles and other items in form of convenient R objects.
	"""
	
	homepage = "https://github.com/szymanskir/hackeRnews"
	cran = "hackeRnews" 

	version("0.1.0", md5="75d6381bfd58245ae1eb68ae95eb4437")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
