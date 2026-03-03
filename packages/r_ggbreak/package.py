# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgbreak(RPackage):
	"""Set Axis Break for 'ggplot2'

	An implementation of scale functions for setting axis breaks of a 'gg' plot.
	"""
	
	homepage = "https://github.com/YuLab-SMU/ggbreak"
	cran = "ggbreak" 

	version("0.1.2", md5="9a8406bf3e2cb3d435ce0b3279e1c978")

	depends_on("r-ggfun@0.1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggplotify@0.0.7:", type=("build", "run"))
	depends_on("r-aplot@0.1.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
