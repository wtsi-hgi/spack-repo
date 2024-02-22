# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDot(RPackage):
	"""Render and Export DOT Graphs in R

	Renders DOT diagram markup language in R and also provides the possibility to
    export the graphs in PostScript and SVG (Scalable Vector Graphics) formats.
    In addition, it supports literate programming packages such as 'knitr' and
    'rmarkdown'.
	"""
	
	homepage = "http://haghish.com/dot"
	cran = "DOT" 

	version("0.1", md5="a1bcb2371fac4210b77177347ec05896")

	depends_on("r-v8@1:", type=("build", "run"))
