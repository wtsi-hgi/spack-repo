# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgrtsy(RPackage):
	"""Add Some Van Gogh Colors and Overlay Colors on Your 'ggplot()'

	Works with 'ggplot2' to add a Van Gogh color palette to the user’s repertoire.
 It also has a function that work alongside 'ggplot2' to create more interesting data visualizations and add contextual information to the user’s plots.
	"""
	
	cran = "ggRtsy" 

	version("0.1.0", md5="510a3f4d6f2c0fa0bdb9166911165edc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
