# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNflplotr(RPackage):
	"""NFL Logo Plots in 'ggplot2' and 'gt'

	A set of functions to visualize National Football League
    analysis in 'ggplot2' plots and 'gt' tables.
	"""
	
	homepage = "https://nflplotr.nflverse.com"
	cran = "nflplotR" 

	version("1.3.1", md5="e65829a7208cc38dd6833d0cacc601be")
	version("1.2.0", md5="a6d5fdc6e25a758b429b569ffd0f4fa6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cachem@1:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-ggpath@1.0.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-gt@0.8:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magick@2.7.3:", type=("build", "run"))
	depends_on("r-memoise@2:", type=("build", "run"))
	depends_on("r-nflreadr@1.3.2:", type=("build", "run"))
	depends_on("r-rappdirs@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
