# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlbplotr(RPackage):
	"""Create 'ggplot2' and 'gt' Visuals with Major League Baseball
Logos

	Tools to help visualize Major League Baseball analysis in 'ggplot2' 
  and 'gt'. You provide team/player information and 'mlbplotR' will transform 
  that information into team colors, logos, or player headshots for graphics.
	"""
	
	homepage = "https://github.com/camdenk/mlbplotR"
	cran = "mlbplotR" 

	version("1.1.0", md5="7b89d4e75164878d5b9a43609b7f2807")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
