# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDandefa(RPackage):
	"""Dandelion Plot for R-Mode Exploratory Factor Analysis

	Contains the function used to create the Dandelion Plot. Dandelion Plot is a visualization method for R-mode Exploratory Factor Analysis. 
	"""
	
	cran = "DandEFA" 

	version("1.6", md5="a975895f14c78531b5d8c05edacbe36d")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
