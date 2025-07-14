# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgfr(RPackage):
	"""Marker Gene Finder in RNA-seq data

	The package is designed to detect marker genes from RNA-seq data.
	"""
	
	bioc = "MGFR"

	version("1.34.0", commit="c71ad8b8c27ce237b3202dcca107078cee2e2f7b")
	version("1.28.0", commit="22ee4944ecd34350f08a3b9238eb070d7ec6ac0b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
