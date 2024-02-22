# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColormap(RPackage):
	"""Color Palettes using Colormaps Node Module

	Allows to generate colors from palettes defined in the colormap module of 'Node.js'. (see <https://github.com/bpostlethwaite/colormap> for more information). In total it provides 44 distinct palettes made from sequential and/or diverging colors. In addition to the pre defined palettes you can also specify your own set of colors. There are also scale functions that can be used with 'ggplot2'.
	"""
	
	homepage = "https://github.com/bhaskarvk/colormap"
	cran = "colormap" 

	version("0.1.4", md5="a8583f94f3cc61b3380df67937f39156")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
