# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROblicubes(RPackage):
	"""3D Rendering Using Obliquely Projected Cubes and Cuboids

	Three-dimensional rendering for 'grid' and 'ggplot2' graphics using cubes and cuboids drawn with an oblique projection.  As a special case also supports primary view orthographic projections.  Can be viewed as an extension to the 'isocubes' package <https://github.com/coolbutuseless/isocubes>.
	"""
	
	homepage = "https://trevorldavis.com/R/oblicubes/"
	cran = "oblicubes" 

	version("0.1.2", md5="b03ea631ace30a43c854d5324b3d8912")

