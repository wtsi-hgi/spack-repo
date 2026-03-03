# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShortcuts(RPackage):
	"""Useful Shortcuts to Interact with 'RStudio' Scripts

	Integrates clipboard copied data in R Studio, loads and installs libraries within a R script and returns all valid arguments of a selected function.
	"""
	
	homepage = "https://github.com/jcval94/shortcuts"
	cran = "shortcuts" 

	version("1.4.0", md5="dcc60f6defdb1611139c2485b632d682")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
