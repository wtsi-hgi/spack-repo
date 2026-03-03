# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgnormalviolin(RPackage):
	"""A 'ggplot2' Extension to Make Normal Violin Plots

	Uses 'ggplot2' to create normally distributed
    violin plots with specified means and standard deviations. This
    function can be useful in showing hypothetically normal distributions
    and confidence intervals.
	"""
	
	homepage = "https://github.com/wjschne/ggnormalviolin"
	cran = "ggnormalviolin" 

	version("0.1.2", md5="92025efe492c1a1b8c8b367cbc8434a9")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
