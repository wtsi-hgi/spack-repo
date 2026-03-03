# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyloclim(RPackage):
	"""Integrating Phylogenetics and Climatic Niche Modeling

	Implements some methods in phyloclimatic modeling: 
  estimation of ancestral climatic niches, age-range-correlation, 
  niche equivalency test and background-similarity test.
	"""
	
	cran = "phyloclim" 

	version("0.9.5", md5="e2d9f11df6468ad0bafb58165600dfe8")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
