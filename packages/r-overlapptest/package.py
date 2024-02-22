# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROverlapptest(RPackage):
	"""Test Overlapping of Polygons Against Random Rotation

	Tests the observed overlapping polygon area in a collection of polygons against a null model of random rotation, as explained in De la Cruz et al. (2017) <doi:10.13140/RG.2.2.12825.72801>.
	"""
	
	cran = "overlapptest" 

	version("1.3", md5="59122b63ac3aa95d7aae4447d49ba6cb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
