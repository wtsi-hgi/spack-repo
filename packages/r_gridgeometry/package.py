# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGridgeometry(RPackage):
	"""Polygon Geometry in 'grid'

	Functions for performing polygon geometry with 'grid' grobs.
             This allows complex shapes to be defined by combining simpler
             shapes.  
	"""
	
	homepage = "https://github.com/pmur002/gridgeometry"
	cran = "gridGeometry" 

	version("0.3-0", md5="9c30860898b744f60c9116da77353b8d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-polyclip@1.10.0:", type=("build", "run"))
