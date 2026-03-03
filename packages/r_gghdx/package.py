# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGghdx(RPackage):
	"""HDX Theme, Scales, and Other Conveniences for 'ggplot2'

	A Humanitarian Data Exchange (HDX) theme, color palettes, and
    scales for 'ggplot2' to allow users to easily follow the HDX visual design
    guide, including convenience functions for for loading and using the
    Source Sans 3 font.
	"""
	
	homepage = "https://github.com/OCHA-DAP/gghdx"
	cran = "gghdx" 

	version("0.1.2", md5="76fce78f55df4b3b0f1bd263cbb7741d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-showtext", type=("build", "run"))
	depends_on("r-sysfonts", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
