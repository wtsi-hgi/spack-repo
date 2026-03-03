# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrigin(RPackage):
	"""Explicitly Qualifying Namespaces by Automatically Adding 'pkg::'
to Functions

	Automatically adding 'pkg::' to a function, i.e. mutate()
    becomes dplyr::mutate(). It is up to the user to determine which
    packages should be used explicitly, whether to include base R packages
    or use the functionality on selected text, a file, or a complete
    directory. User friendly logging is provided in the 'RStudio' Markers
    pane. Lives in the spirit of 'lintr' and 'styler'. Can also be used
    for checking which packages are actually used in a project.
	"""
	
	homepage = "https://github.com/mnist91/origin"
	cran = "origin" 

	version("1.1.1", md5="b96f3d07b053311cd5b494e6ef430c4e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
