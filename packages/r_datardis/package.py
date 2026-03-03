# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatardis(RPackage):
	"""Data from the Doctor Who Series

	Explore data related to the Doctor Who TV series.
	"""
	
	cran = "datardis" 

	version("0.0.4", md5="0dc08a877c67b0461623e0a32fee3cc1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
