# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioassays(RPackage):
	"""Summarising Multi Well Plate Cellular Assay

	The goal is to help users to analyse data from multi wells with minimum effort. Using these functions several plates can be analyzed automatically.
	"""
	
	cran = "bioassays" 

	version("1.0.1", md5="af40378c5ec95ccd785f5c282aaf4205")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nplr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
