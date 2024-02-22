# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidylpa(RPackage):
	"""Easily Carry Out Latent Profile Analysis (LPA) Using Open-Source
or Commercial Software

	An interface to the 'mclust' package to easily
    carry out latent profile analysis ("LPA"). Provides functionality to
    estimate commonly-specified models. Follows a tidy approach, in that
    output is in the form of a data frame that can subsequently be
    computed on. Also has functions to interface to the commercial 'MPlus'
    software via the 'MplusAutomation' package.
	"""
	
	homepage = "https://data-edu.github.io/tidyLPA/"
	cran = "tidyLPA" 

	version("1.1.0", md5="d81f423730e45a1148c4036533a077cf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mix", type=("build", "run"))
	depends_on("r-mplusautomation", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
