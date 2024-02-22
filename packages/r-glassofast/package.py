# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlassofast(RPackage):
	"""Fast Graphical LASSO

	A fast and improved implementation of the graphical LASSO.
	"""
	
	cran = "glassoFast" 

	version("1.0.1", md5="fb6b3a5745350df1367fe57df8698e9e")

