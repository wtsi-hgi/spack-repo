# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGridtext(RPackage):
	"""Improved Text Rendering Support for 'Grid' Graphics

	Provides support for rendering of formatted text using 'grid' graphics. Text can be
    formatted via a minimal subset of 'Markdown', 'HTML', and inline 'CSS' directives, and it can be
    rendered both with and without word wrap.
	"""
	
	homepage = "https://wilkelab.org/gridtext/"
	cran = "gridtext" 

	version("0.1.5", md5="44f9ed1aa457f491b48901521cbfa1d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
