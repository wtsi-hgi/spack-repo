# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgh4x(RPackage):
	"""Hacks for 'ggplot2'

	A 'ggplot2' extension that does a variety of little
    helpful things.  The package extends 'ggplot2' facets through
    customisation, by setting individual scales per panel, resizing panels
    and providing nested facets.  Also allows multiple colour and fill
    scales per plot. Also hosts a smaller collection of stats, geoms and axis 
    guides.
	"""
	
	homepage = "https://github.com/teunbrand/ggh4x"
	cran = "ggh4x" 

	version("0.2.8", md5="495cbc3a454dc6e898094d384a58246c")

	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-vctrs@0.5:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
