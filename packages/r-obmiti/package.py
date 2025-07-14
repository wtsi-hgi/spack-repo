# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObmiti(RPackage):
	"""Ob/ob Mice Data on Normal and High Fat Diet

	The package provide RNA-seq count for 2 strains of mus musclus; Wild type and Ob/Ob. Each strain was divided into two groups, and each group received either chow diet or high fat diet. RNA expression was measured after 20 weeks in 7 tissues.
	"""
	
	homepage = "https://github.com/OmarElAshkar/ObMiTi"
	bioc = "ObMiTi"

	version("1.16.0", commit="8507da8b36d1ea2767392f893e7b4300fb38269f")
	version("1.10.0", commit="765fe6ca16d607c1f229203efd5f27272f46784a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

