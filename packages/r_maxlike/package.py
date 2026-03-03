# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaxlike(RPackage):
	"""Model Species Distributions by Estimating the Probability of
Occurrence Using Presence-Only Data

	Provides a likelihood-based approach to modeling species distributions using presence-only data. In contrast to the popular software program MAXENT, this approach yields estimates of the probability of occurrence, which is a natural descriptor of a species' distribution.
	"""
	
	cran = "maxlike" 

	version("0.1-11", md5="763905354f3ea3bef9728f39d8a4604f")
	version("0.1-10", md5="9625ea87bb61a8753b06b65eaab0a306")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
