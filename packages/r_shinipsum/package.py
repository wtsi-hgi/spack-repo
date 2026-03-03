# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinipsum(RPackage):
	"""Lorem-Ipsum-Like Helpers for Fast Shiny Prototyping

	Prototype your shiny apps quickly with these
    Lorem-Ipsum-like Helpers.
	"""
	
	homepage = "https://github.com/Thinkr-open/shinipsum"
	cran = "shinipsum" 

	version("0.1.1", md5="3876c87ddbb08de3cab978a23a4044fb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-attempt", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
