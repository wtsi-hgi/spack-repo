# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgs(RPackage):
	"""Crosswalk Municipality and District Statistics in Germany

	Construct time series for Germany's municipalities (Gemeinden) and districts (Kreise) using a annual crosswalk constructed by the Federal Office for Building and Regional Planning (BBSR). 
	"""
	
	homepage = "https://sumtxt.github.io/ags/"
	cran = "ags" 

	version("1.0.1", md5="dd1db50fdf01388760afbeb88a70e706")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rlang@1.0.4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
