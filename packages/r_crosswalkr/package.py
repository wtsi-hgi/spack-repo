# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrosswalkr(RPackage):
	"""Rename and Encode Data Frames Using External Crosswalk Files

	A pair of functions for renaming and encoding data frames
	     using external crosswalk files. It is especially useful when
	     constructing master data sets from multiple smaller data
	     sets that do not name or encode variables consistently
	     across files. Based on similar commands in 'Stata'.
	"""
	
	homepage = "https://github.com/btskinner/crosswalkr"
	cran = "crosswalkr" 

	version("0.2.6", md5="ed67371ad22b09f5f6a4555cc1ca8d73")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
