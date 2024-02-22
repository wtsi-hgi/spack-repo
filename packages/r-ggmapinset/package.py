# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmapinset(RPackage):
	"""Add Inset Panels to Maps

	Helper to add insets based on geom_sf() from 'ggplot2'.
    This package gives you a drop-in replacement for geom_sf() that supports
    adding a zoomed inset map without having to create and embed a separate plot.
	"""
	
	homepage = "https://github.com/cidm-ph/ggmapinset"
	cran = "ggmapinset" 

	version("0.3.0", md5="eecbb2b585a8a28c78eda2c6ff455c7a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
