# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGseg(RPackage):
	"""Graph-Based Change-Point Detection (g-Segmentation)

	Using an approach based on similarity graph to estimate change-point(s) and the corresponding p-values.  Can be applied to any type of data (high-dimensional, non-Euclidean, etc.) as long as a reasonable similarity measure is available.
	"""
	
	cran = "gSeg" 

	version("1.0", md5="be69208b459f1e7eb07b2783071943dd")

	depends_on("r@3.0.1:", type=("build", "run"))
