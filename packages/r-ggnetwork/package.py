# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgnetwork(RPackage):
	"""Geometries to Plot Networks with 'ggplot2'

	Geometries to plot network objects with 'ggplot2'.
	"""
	
	homepage = "https://github.com/briatte/ggnetwork"
	cran = "ggnetwork" 

	version("0.5.13", md5="d65ad1b00fb6fef73dca03841285b5d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-ggrepel@0.5:", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
