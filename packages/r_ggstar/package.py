# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgstar(RPackage):
	"""Multiple Geometric Shape Point Layer for 'ggplot2'

	To create the multiple polygonal point layer for easily discernible shapes, 
             we developed the package, it is like the 'geom_point' of 'ggplot2'.
             It can be used to draw the scatter plot.
	"""
	
	homepage = "https://github.com/xiangpin/ggstar/"
	cran = "ggstar" 

	version("1.0.4", md5="bf91c49939cf67a29d82bb526451ef6b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
