# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmake(RPackage):
	"""Makefile Generator for R Analytical Projects

	Creates and maintains a build process for complex analytic tasks in R.
  Package allows to easily generate Makefile for the (GNU) 'make' tool, which drives the build process
  by (in parallel) executing build commands in order to update results accordingly to given dependencies
  on changed data or updated source files.
	"""
	
	cran = "rmake" 

	version("1.1.0", md5="86f7b7f42bd22d0845a3c26de6a82f18")

	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
