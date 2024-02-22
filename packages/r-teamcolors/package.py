# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTeamcolors(RPackage):
	"""Color Palettes for Pro Sports Teams

	Provides color palettes corresponding to professional and amateur, 
    sports teams. These can be useful in creating data graphics that are themed 
    for particular teams. 
	"""
	
	homepage = "http://github.com/beanumber/teamcolors"
	cran = "teamcolors" 

	version("0.0.4", md5="c4ed6265ab4d9153eb703c72eee9d5f8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
