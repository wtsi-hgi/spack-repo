# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForagingorg(RPackage):
	"""Organization Measures for Visual Foraging

	Several functions to compute indicators for organization and efficiency in visual foraging, multi-target visual search, and cancellation tasks. The current version of this package includes the following indicators: best-r, mean Inter-target Distance, Percentage Above Optimal (PAO) scan path, and intersections in the scan path. For more detailed descriptions, see Mark et al. (2004) <doi:10.1212/01.WNL.0000131947.08670.D4>.
	"""
	
	cran = "ForagingOrg" 

	version("0.1.0", md5="b916f6b7d9a397a7e4bd8f4de51d65b7")

	depends_on("r-pairviz", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
