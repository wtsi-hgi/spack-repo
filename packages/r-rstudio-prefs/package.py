# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstudioPrefs(RPackage):
	"""Set 'RStudio' Preferences

	As of 'RStudio' v1.3, the preferences in the Global Options
    dialog (and a number of other preferences that aren’t) are now saved
    in simple, plain-text JSON files. This package provides an interface
    for working with these 'RStudio' JSON preference files to easily make
    modifications without using the point-and-click option menus. This is
    particularly helpful when working on teams to ensure a unified
    experience across machines and utilizing settings for best practices.
	"""
	
	homepage = "https://github.com/ddsjoberg/rstudio.prefs"
	cran = "rstudio.prefs" 

	version("0.1.9", md5="ec6a633a8e7901f14f21a65f31334659")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli@2.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-fs@1.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rappdirs@0.3.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-rstudioapi@0.13:", type=("build", "run"))
	depends_on("r-rvest@1:", type=("build", "run"))
	depends_on("r-tibble@3.1.2:", type=("build", "run"))
