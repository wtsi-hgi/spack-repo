# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtext(RPackage):
	"""Improved Text Rendering Support for 'ggplot2'

	A 'ggplot2' extension that enables the rendering of
    complex formatted plot labels (titles, subtitles, facet labels,
    axis labels, etc.). Text boxes with automatic word wrap are also
    supported.
	"""
	
	homepage = "https://wilkelab.org/ggtext/"
	cran = "ggtext" 

	version("0.1.2", md5="fb0b751ae1d0cb66c7e75006c3cf8cc7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-gridtext", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
