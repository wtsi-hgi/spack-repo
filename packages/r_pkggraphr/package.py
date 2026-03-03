# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkggraphr(RPackage):
	"""Graph the Relationship Between Functions in an R Package

	It is often useful when developing an R package to track the relationship between functions in order to appropriately test and track changes. This package generates a graph of the relationship between all R functions in a package. It can also be used on any directory containing .R files which can be very useful for 'shiny' apps or other non-package workflows. 
	"""
	
	homepage = "https://gitlab.com/doliv071/pkggraphr"
	cran = "pkgGraphR" 

	version("0.2.0", md5="3e58aa50f09e6942b33c64f513677378")

	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
