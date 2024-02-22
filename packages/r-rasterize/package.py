# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasterize(RPackage):
	"""Rasterize Graphical Output

	Provides R functions to selectively rasterize components
             of 'grid' output.  
	"""
	
	homepage = "https://github.com/pmur002/rasterize"
	cran = "rasterize" 

	version("0.1", md5="2b0e45b695d5a3a1c7e02778df25088b")

	depends_on("r-png", type=("build", "run"))
