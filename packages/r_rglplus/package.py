# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRglplus(RPackage):
	"""Extension of the 'rgl' 3D Visualization Package

	Provides 3D plotting routines that facilitate the use of the 'rgl' package and extend its functionality. For example, the routines allow the user to directly control the camera position & orientation, as well as to generate 3D movies with a moving observer.
	"""
	
	cran = "rglplus" 

	version("1.1", md5="f2fa77c43028eeca64fbecc77a6a33cf")

	depends_on("r-rgl", type=("build", "run"))
