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

	version("0.3.0", md5="e527f27c933818bc6490b209d8dba54f")
	version("0.2.8", md5="495cbc3a454dc6e898094d384a58246c")

	with default_args(type=("build", "run")):
		depends_on("r-ggplot2@3.5:", when="@0.3.0:")
		depends_on("r-ggplot2@3.4.2:3.4", when="@0.2.8")
		depends_on("r-gtable")
		depends_on("r-scales")
		depends_on("r-vctrs@0.5:")
		depends_on("r-rlang@1.1:")
		depends_on("r-lifecycle")
		depends_on("r-cli")
