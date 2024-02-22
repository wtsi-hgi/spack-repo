# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdhfm(RPackage):
	"""Variance Stabilization by Data-Driven Haar-Fisz (for
Microarrays)

	Contains the normalizing and variance stabilizing
	Data-Driven Haar-Fisz algorithm. Also contains related algorithms
	for simulating from certain microarray gene intensity models and
	evaluation of certain transformations. Contains cDNA and shipping
	credit flow data.
	"""
	
	cran = "DDHFm" 

	version("1.1.3", md5="065a6fd19f521989cf9b67340bc0cbda")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lokern", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
