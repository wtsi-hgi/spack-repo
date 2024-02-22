# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMldr(RPackage):
	"""Exploratory Data Analysis and Manipulation of Multi-Label Data
Sets

	Exploratory data analysis and manipulation functions for multi-
    label data sets along with an interactive Shiny application to ease their use.
	"""
	
	homepage = "https://github.com/fcharte/mldr"
	cran = "mldr" 

	version("0.4.3", md5="ac41d31c4344b47faa505a6899d7768f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-shiny@0.11:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
