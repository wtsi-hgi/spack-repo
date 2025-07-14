# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDexmadata(RPackage):
	"""Data package for DExMA package

	Data objects needed to allSameID() function of DExMA package. There are also some objects that are necessary to be able to apply the examples of the DExMA package, which illustrate package functionality.
	"""
	
	bioc = "DExMAdata"

	version("1.16.0", commit="78b9533c9787a789df3e93394d1bcb7207507e5a")
	version("1.10.0", commit="3d2144d85e2f7d8e7039add20ff5b7851017d4d7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

