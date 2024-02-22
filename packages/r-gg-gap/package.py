# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgGap(RPackage):
	"""Define Segments in y-Axis for 'ggplot2'

	It is not very easy to define segments for y-axis in a 'ggplot2' plot. gg.gap() function in this package can carry it out.
	"""
	
	homepage = "https://github.com/ChrisLou-bioinfo/gg.gap"
	cran = "gg.gap" 

	version("1.3", md5="a22be06d599f5942d6c58663976a3f0c")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
