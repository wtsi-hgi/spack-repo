# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTealLogger(RPackage):
	"""Logging Setup for the 'teal' Family of Packages

	
    Utilizing the 'logger' framework to record events within a package, specific to 'teal' family of packages.
    Supports logging namespaces, hierarchical logging, various log destinations, vectorization, and more.
	"""
	
	cran = "teal.logger" 

	version("0.1.3", md5="c67a93b12c0612a9f661686f5dff5772")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-logger@0.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
