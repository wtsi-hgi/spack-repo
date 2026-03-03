# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanvasxpress(RPackage):
	"""Visualization Package for CanvasXpress in R

	Enables creation of visualizations using the CanvasXpress framework
    in R. CanvasXpress is a standalone JavaScript library for reproducible research
    with complete tracking of data and end-user modifications stored in a single
    PNG image that can be played back. See <https://www.canvasxpress.org> for more
    information.
	"""
	
	homepage = "https://github.com/neuhausi/canvasXpress"
	cran = "canvasXpress" 

	version("1.46.9-1", md5="f25e77795fcb5dc87488793b343c60e0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-htmlwidgets@1:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
