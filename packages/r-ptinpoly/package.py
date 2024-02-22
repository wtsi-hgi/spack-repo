# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtinpoly(RPackage):
	"""Point-in-Polyhedron Test (2D and 3D)

	Function pip3d() tests whether a point in 3D space is
  within, exactly on, or outside an enclosed surface defined by a triangular mesh.
  Function pip2d() tests whether a point in 2D space is within, exactly on, or outside a polygon.
  For a reference, see: Liu et al., A new point containment test algorithm based on preprocessing
  and determining triangles, Computer-Aided Design 42(12):1143-1150.
	"""
	
	homepage = "http://ptinpoly.pbworks.com"
	cran = "ptinpoly" 

	version("2.8", md5="efaf1c749303fe0e92525710cb7e1fed")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
