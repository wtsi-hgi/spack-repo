# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMakepalette(RPackage):
	"""Make Palette

	Functions that allow you to create your own color palette from an image, using mathematical algorithms.
	"""
	
	homepage = "https://github.com/musajajorge/makePalette"
	cran = "makePalette" 

	version("0.1.2", md5="8c42e817c316fa8a1e47f27fca061fc3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-prismatic", type=("build", "run"))
