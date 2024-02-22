# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REqualdenHd(RPackage):
	"""Testing the Equality of a High Dimensional Set of Densities

	The equality of a large number k of densities is tested by measuring the L2 distance between the corresponding kernel density estimators and the one based on the pooled sample. The test even works for sample sizes as small as 2.
	"""
	
	cran = "Equalden.HD" 

	version("1.2", md5="0b322d745e573f5ff997a2467103cdd5")

	depends_on("r@3.4:", type=("build", "run"))
