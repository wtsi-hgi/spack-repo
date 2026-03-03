# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsicons(RPackage):
	"""Easily Work with 'Bootstrap' Icons

	Easily use 'Bootstrap' icons inside 'Shiny' apps and 'R
    Markdown' documents. More generally, icons can be inserted in any
    'htmltools' document through inline 'SVG'.
	"""
	
	homepage = "https://github.com/rstudio/bsicons"
	cran = "bsicons" 

	version("0.1.2", md5="bc01c2d201744fe791e7d2e9cd7434f2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
