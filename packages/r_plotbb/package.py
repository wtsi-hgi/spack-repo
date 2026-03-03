# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotbb(RPackage):
	"""Grammar of Graphics for 'base' Plot

	Proof of concept for implementing grammar of graphics using base plot. The bbplot() function initializes a 'bbplot' object to store input data, aesthetic mapping, a list of layers and theme elements. The object will be rendered as a graphic using base plot command if it is printed.  
	"""
	
	cran = "plotbb" 

	version("0.0.6", md5="30508f279d32d76277c957e1f6c1bb7a")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
