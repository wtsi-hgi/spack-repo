# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactran(RPackage):
	"""Reactive Transport Modelling in 1d, 2d and 3d

	Routines for developing models that describe reaction and advective-diffusive transport in one, two or three dimensions.
  Includes transport routines in porous media, in estuaries, and in bodies with variable shape.
	"""
	
	cran = "ReacTran" 

	version("1.4.3.1", md5="7b875d7d16ab1269890fee743a3c8190")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
