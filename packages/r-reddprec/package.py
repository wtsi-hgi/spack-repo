# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReddprec(RPackage):
	"""Reconstruction of Daily Data - Precipitation

	Applies quality control to daily precipitation observations; 
    reconstructs the original series by estimating precipitation in missing values; and 
    creates gridded datasets of daily precipitation.
	"""
	
	cran = "reddPrec" 

	version("2.0.1", md5="7d0caf9099ab7814342cef6ebcd77335")

	depends_on("r-terra", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-qmap", type=("build", "run"))
