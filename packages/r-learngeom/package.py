# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLearngeom(RPackage):
	"""Learning Plane Geometry

	Contains some functions to learn and teach basic plane Geometry at undergraduate level with the aim of being helpful to young students with little programming skills.
	"""
	
	cran = "LearnGeom" 

	version("1.5", md5="5088804c0745412d8fccc884cea9dd78")

	depends_on("r@3.0.2:", type=("build", "run"))
