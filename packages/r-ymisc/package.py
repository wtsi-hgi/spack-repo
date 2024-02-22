# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYmisc(RPackage):
	"""Miscellaneous Functions

	The Author's personal R Package that contains miscellaneous functions. 
    The current version of package contains miscellaneous functions for brain data 
    to compute Asymmetry Index (AI) and bilateral (L+R) measures and reshape the data.
	"""
	
	cran = "Ymisc" 

	version("0.1.0", md5="9dc8e45bab94e9c43a36c24c86f7637b")

	depends_on("r@3.5:", type=("build", "run"))
