# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodemeta(RPackage):
	"""A Smaller 'codemetar' Package

	The 'Codemeta' Project defines a 'JSON-LD' format
    for describing software metadata, as detailed at
    <https://codemeta.github.io>. This package provides core utilities
    to generate this metadata with a minimum of dependencies.
	"""
	
	homepage = "https://github.com/cboettig/codemeta"
	cran = "codemeta" 

	version("0.1.1", md5="2c37e6b4aa736d3218b43826283cbf17")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
