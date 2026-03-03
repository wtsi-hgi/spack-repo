# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSphereplot(RPackage):
	"""Spherical Plotting

	Various functions for creating spherical coordinate system plots via extensions to rgl.
	"""
	
	cran = "sphereplot" 

	version("1.5.1", md5="5364d492cd67c40395cc787d0bcc836f")

	depends_on("r-rgl", type=("build", "run"))
