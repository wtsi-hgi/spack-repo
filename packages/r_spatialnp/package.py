# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialnp(RPackage):
	"""Multivariate Nonparametric Methods Based on Spatial Signs and
Ranks

	Test and estimates of location, tests of independence, tests of sphericity and several estimates of shape all based on spatial signs, symmetrized signs, ranks and signed ranks. For details, see Oja and Randles (2004) <doi:10.1214/088342304000000558> and Oja (2010) <doi:10.1007/978-1-4419-0468-3>.
	"""
	
	cran = "SpatialNP" 

	version("1.1-5", md5="63b81d5a1ad7188281dbb5b5fc24c4c4")

	depends_on("r@2.4:", type=("build", "run"))
