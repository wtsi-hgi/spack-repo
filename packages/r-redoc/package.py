# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedoc(RPackage):
	"""Generates 'Redoc' Documentation from an 'OpenAPI' Specification

	A collection of 'HTML', 'JavaScript', 'CSS' and fonts
  assets that generate 'Redoc' documentation from an 'OpenAPI' Specification:
   <https://redocly.com/redoc/>.
	"""
	
	homepage = "https://github.com/meztez/redoc"
	cran = "redoc" 

	version("2.0.0.75", md5="7b82a4ca624537588053d602847c60c5")

	depends_on("r-jsonlite", type=("build", "run"))
