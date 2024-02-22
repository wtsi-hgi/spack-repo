# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdxtrees(RPackage):
	"""Data Package of Portland, Oregon Trees

	An engaging collection of datasets from Portland Parks and Recreation. The city of Portland inventoried every tree in over 170 parks and along the streets in 96 neighborhoods. 
	"""
	
	homepage = "https://github.com/mcconvil/pdxTrees"
	cran = "pdxTrees" 

	version("0.4.0", md5="81b11fa0bf4eea4c03aa46378382eb84")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
