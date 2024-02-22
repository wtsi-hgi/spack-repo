# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcss(RPackage):
	"""Cluster Circular Systematic Sampling

	Draws systematic samples from a population that follows linear trend. The function returns a matrix comprising of the required samples as its column vectors. The samples produced are highly efficient and the inter sampling variance is minimum. The scheme will be useful in various field like Bioinformatics where the samples are expensive and must be precise in reflecting the population by possessing least sampling variance.
	"""
	
	cran = "ccss" 

	version("1.0", md5="6f50c1a931c9ad14685847d2e1db5800")

	depends_on("r@2.10:", type=("build", "run"))
