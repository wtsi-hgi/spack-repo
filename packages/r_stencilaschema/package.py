# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStencilaschema(RPackage):
	"""Bindings for Stencila Schema

	Provides R bindings for the Stencila Schema <https://schema.stenci.la>. This package is primarily aimed at R developers wanting to programmatically generate, or modify, executable documents.
	"""
	
	homepage = "https://github.com/stencila/schema#readme"
	cran = "stencilaschema" 

	version("1.0.0", md5="3a81c48a70afd38061080f7d3ed38da0")

