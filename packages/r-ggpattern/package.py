# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpattern(RPackage):
	"""'ggplot2' Pattern Geoms

	Provides 'ggplot2' geoms filled with various patterns.  Includes a patterned version of every 'ggplot2' geom that has a region that can be filled with a pattern.  Provides a suite of 'ggplot2' aesthetics and scales for controlling pattern appearances.  Supports over a dozen builtin patterns (every pattern implemented by 'gridpattern') as well as allowing custom user-defined patterns.
	"""
	
	homepage = "https://github.com/coolbutuseless/ggpattern"
	cran = "ggpattern" 

	version("1.0.1", md5="77c506ff95415135824f34dd6e0b515c")

	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-gridpattern@1.0.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
