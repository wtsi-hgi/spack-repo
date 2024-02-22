# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSphereoptimize(RPackage):
	"""Optimization on a Unit Sphere

	A simple tool for numerical optimization on the unit sphere. This is achieved by combining the spherical coordinating system with L-BFGS-B optimization. This algorithm is implemented in Kolkiewicz, A., Rice, G., & Xie, Y. (2020) <doi:10.1016/j.jspi.2020.07.001>. 
	"""
	
	cran = "SphereOptimize" 

	version("0.1.1", md5="33fe46dc2d689cad584c61f79822af10")

