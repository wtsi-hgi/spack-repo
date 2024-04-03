# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTealLogger(RPackage):
	"""Logging Setup for the 'teal' Family of Packages

	Utilizing the 'logger' framework to record events within a
    package, specific to 'teal' family of packages.  Supports logging
    namespaces, hierarchical logging, various log destinations,
    vectorization, and more.
	"""
	
	homepage = "https://insightsengineering.github.io/teal.logger/"
	cran = "teal.logger" 

	version("0.2.0", md5="4ade45cdf34222012d3ded7cc2b1a751")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-glue@1:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-logger@0.2:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-withr@2.1:", type=("build", "run"))
