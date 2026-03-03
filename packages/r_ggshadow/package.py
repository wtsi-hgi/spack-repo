# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgshadow(RPackage):
	"""Shadow and Glow Geoms for 'ggplot2'

	A collection of Geoms for R's 'ggplot2' library. geom_shadowpath(), geom_shadowline(), 
    geom_shadowstep() and geom_shadowpoint() functions draw a shadow below lines to make busy plots more 
    aesthetically pleasing. geom_glowpath(), geom_glowline(), geom_glowstep() and geom_glowpoint() add a 
    neon glow around lines to get a steampunk style.
	"""
	
	homepage = "https://github.com/marcmenem/ggshadow/"
	cran = "ggshadow" 

	version("0.0.5", md5="54128d73b01c2e36533b65a108676401")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
