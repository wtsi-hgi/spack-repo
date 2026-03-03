# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPostdoc(RPackage):
	"""Minimal and Uncluttered Package Documentation

	Generates simple and beautiful one-page HTML reference manuals 
    with package documentation. Math rendering and syntax highlighting are done 
    server-side in R such that no JavaScript libraries are needed in the
    browser, which makes the documentation portable and fast to load.
	"""
	
	homepage = "https://ropensci.r-universe.dev/postdoc"
	cran = "postdoc" 

	version("1.2.2", md5="b43edd3deaab6e28c51a698a76fa753c")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-katex", type=("build", "run"))
	depends_on("r-prismjs", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
