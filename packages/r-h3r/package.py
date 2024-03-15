# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH3r(RPackage):
	"""Hexagonal Hierarchical Geospatial Indexing System

	Provides access to Uber's 'H3' geospatial indexing system via 'h3lib' 
  <https://CRAN.R-project.org/package=h3lib>. 'h3r' is designed to mimic the 'H3' 
  Application Programming Interface (API) <https://h3geo.org/docs/api/indexing/>, 
  so that any function in the API is also available in 'h3r'.
	"""
	
	homepage = "https://symbolixau.github.io/h3r/"
	cran = "h3r" 

	version("0.1.1", md5="f3215b910dc00e49b1eef805a876e14f")

	depends_on("r-h3lib", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
