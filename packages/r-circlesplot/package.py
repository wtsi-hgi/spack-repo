# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCirclesplot(RPackage):
	"""Visualize Proportions with Circles in a Plot

	Method for visualizing proportions between objects of different sizes. 
    The proportions are drawn as circles with different diameters, which makes them ideal
    for visualizing proportions between planets.
	"""
	
	homepage = "https://github.com/BenSt099/circlesplot"
	cran = "circlesplot" 

	version("1.1.0", md5="b11853b0b4ef57f06289c2a4f8382864")

	depends_on("r-plotrix", type=("build", "run"))
