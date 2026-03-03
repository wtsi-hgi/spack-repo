# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpackets(RPackage):
	"""Package Plot Layers for Easier Portability and Modularization

	
    Create groups of 'ggplot2' layers that can be easily migrated from one plot
    to another, reducing redundant code and improving the ability to format many
    plots that draw from the same source 'ggpacket' layers.
	"""
	
	homepage = "https://github.com/dgkf/ggpackets"
	cran = "ggpackets" 

	version("0.2.1", md5="88ff03fd1f152e2bd1ee430faf666d54")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
