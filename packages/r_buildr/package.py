# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBuildr(RPackage):
	"""Organize & Run Build Scripts Comfortably

	Working with reproducible reports or any other
    similar projects often require to run the script that builds the
    output file in a specified way. 'buildr' can help you organize, modify
    and comfortably run those scripts. The package provides a set of
    functions that interactively guides you through the process and that
    are available as 'RStudio' Addin, meaning you can set up the keyboard
    shortcuts, enabling you to choose and run the desired build script
    with one keystroke anywhere anytime.
	"""
	
	homepage = "https://netique.github.io/buildr/"
	cran = "buildr" 

	version("0.1.1", md5="4e4e1f7376a744086adf7ba335631188")

	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
