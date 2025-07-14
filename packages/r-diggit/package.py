# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiggit(RPackage):
	"""Inference of Genetic Variants Driving Cellular Phenotypes

	Inference of Genetic Variants Driving Cellullar Phenotypes by the DIGGIT algorithm
	"""
	
	bioc = "diggit"

	version("1.40.0", commit="da51ac60ea1e82c003ec977500f8bdf23211b748")
	version("1.34.0", commit="ad5750736d70b04401f0f28963bb851f99735f40")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-viper@1.3.1:", type=("build", "run"))
