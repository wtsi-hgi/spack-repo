# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnorfuzzy(RPackage):
	"""Addon to CellNOptR: Fuzzy Logic

	This package is an extension to CellNOptR.  It contains additional functionality needed to simulate and train a prior knowledge network to experimental data using constrained fuzzy logic (cFL, rather than Boolean logic as is the case in CellNOptR).  Additionally, this package will contain functions to use for the compilation of multiple optimization results (either Boolean or cFL).
	"""
	
	bioc = "CNORfuzzy"

	version("1.50.0", commit="37ae261365479afdab5e306c5bd56b5fc47bb449")
	version("1.44.0", commit="c3b7b6ac649692c9aa0078672c19c3cc9972ceee")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-cellnoptr@1.4:", type=("build", "run"))
	depends_on("r-nloptr@0.8.5:", type=("build", "run"))
