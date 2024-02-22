# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgfx(RPackage):
	"""Pixel Filters for 'ggplot2' and 'grid'

	Provides a range of filters that can be applied to layers from the 
    'ggplot2' package and its extensions, along with other graphic elements such 
    as guides and theme elements. The filters are applied at render time and 
    thus uses the exact pixel dimensions needed.
	"""
	
	homepage = "https://ggfx.data-imaginist.com"
	cran = "ggfx" 

	version("1.0.1", md5="6d450a409494eb4d15e7506712ccf5ac")

	depends_on("r-magick@2.7.1:", type=("build", "run"))
	depends_on("r-ragg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
