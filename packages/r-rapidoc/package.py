# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapidoc(RPackage):
	"""Generates 'RapiDoc' Documentation from an 'OpenAPI'
Specification

	A collection of 'HTML', 'JavaScript', 'CSS' and fonts
  assets that generate 'RapiDoc' documentation from an 'OpenAPI' Specification:
   <https://mrin9.github.io/RapiDoc/>.
	"""
	
	homepage = "https://github.com/meztez/rapidoc"
	cran = "rapidoc" 

	version("9.3.4", md5="551db0ce8a6bf03adbdd52eb43ccd1bb")

