# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLemon(RPackage):
	"""Freshing Up your 'ggplot2' Plots

	Functions for working with legends and axis lines of 'ggplot2',
    facets that repeat axis lines on all panels, and some 'knitr' extensions.
	"""
	
	homepage = "https://github.com/stefanedwards/lemon"
	cran = "lemon" 

	version("0.4.9", md5="002d07206e4f433ad152895533bb1258")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-knitr@1.12:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
