# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighlight(RPackage):
	"""Syntax Highlighter

	Syntax highlighter for R code based on the results of the R
    parser. Rendering in HTML and latex markup. Custom Sweave driver
    performing syntax highlighting of R code chunks.
	"""
	
	homepage = "https://github.com/hadley/highlight"
	cran = "highlight" 

	version("0.5.1", md5="d9a0bf21b67e6ded29c9505bc800b436")

	depends_on("r@3.2:", type=("build", "run"))
