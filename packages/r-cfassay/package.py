# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfassay(RPackage):
	"""Statistical analysis for the Colony Formation Assay

	The package provides functions for calculation of linear-quadratic cell survival curves and for ANOVA of experimental 2-way designs along with the colony formation assay.
	"""
	
	bioc = "CFAssay"

	version("1.42.0", commit="2bd2bae1dccab81e441b19e058b12ff4fbb738e8")
	version("1.36.0", commit="e3d3b297ac2af51625d8a8fa36b8ee8b86d667ac")

	depends_on("r@2.10:", type=("build", "run"))
