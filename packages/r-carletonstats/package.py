# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarletonstats(RPackage):
	"""Functions for Statistics Classes at Carleton College

	Includes commands for bootstrapping and permutation tests, a
    command for created grouped bar plots, and a demo of the
    quantile-normal plot for data drawn from different distributions.
	"""
	
	homepage = "https://github.com/aloy/CarletonStats"
	cran = "CarletonStats" 

	version("2.2", md5="87c9387fd61249e8d2de24a1271163c4")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
