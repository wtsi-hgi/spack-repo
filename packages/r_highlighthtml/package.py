# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighlighthtml(RPackage):
	"""Highlight HTML Text and Tables

	A tool to format R markdown with CSS ids for HTML output. 
    The tool may be most helpful for those using markdown to create reproducible
    documents. The biggest limitations in formatting is the knowledge of CSS
    by the document authors.
	"""
	
	homepage = "https://github.com/lebebr01/highlightHTML"
	cran = "highlightHTML" 

	version("0.2.5", md5="73be2a244228a9a5eec0000d01f8e5c5")

	depends_on("r@3:", type=("build", "run"))
