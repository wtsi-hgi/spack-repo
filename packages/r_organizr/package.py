# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrganizr(RPackage):
	"""Shortcuts for File Creation with Informative Prefixes

	Provides functions for quickly creating R and Python scripts, as 
    well as 'Rmarkdown' or Quarto documents with automatically assigned name 
    prefixes. Prefixes are either file counts (e.g. "001") or dates 
    (e.g. "2022-09-26").
	"""
	
	homepage = "https://github.com/jobrachem/organizr"
	cran = "organizr" 

	version("0.1.0", md5="7945c509735c548a607659b8ab21de74")

	depends_on("r-fs", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
