# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrismatic(RPackage):
	"""Color Manipulation Tools

	Manipulate and visualize colors in a intuitive,
    low-dependency and functional way.
	"""
	
	homepage = "https://github.com/EmilHvitfeldt/prismatic"
	cran = "prismatic" 

	version("1.1.1", md5="9b1eb9811f9c3a938f854e5a41c5f60b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-farver@2.0.1:", type=("build", "run"))
