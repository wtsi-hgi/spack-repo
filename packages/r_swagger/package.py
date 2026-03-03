# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwagger(RPackage):
	"""Dynamically Generates Documentation from a 'Swagger' Compliant
API

	A collection of 'HTML', 'JavaScript', and 'CSS' assets that
  dynamically generate beautiful documentation from a 'Swagger' compliant API:
  <https://swagger.io/specification/>.
	"""
	
	homepage = "https://github.com/rstudio/swagger"
	cran = "swagger" 

	version("3.33.1", md5="cf824d9879735a56fbd783828373a9f3")

