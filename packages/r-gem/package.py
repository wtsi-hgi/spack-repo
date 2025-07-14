# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGem(RPackage):
	"""GEM: fast association study for the interplay of Gene, Environment and Methylation

	Tools for analyzing EWAS, methQTL and GxE genome widely.
	"""
	
	bioc = "GEM"

	version("1.34.0", commit="eaa8b95c440ed581800ed53f832fbc2d5bc60569")
	version("1.28.0", commit="fe6542f5f16d1b86483ea3ed615116199b647999")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
