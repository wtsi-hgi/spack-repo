# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSocialh(RPackage):
	"""Rank and Social Hierarchy for Gregarious Animals

	Tools developed to facilitate the establishment of the rank and social hierarchy 
             for gregarious animals by the Si method developed by 
             Kondo & Hurnik (1990)<doi:10.1016/0168-1591(90)90125-W>. It is
             also possible to determine the number of agonistic interactions between two 
             individuals, sociometric and dyadics matrix from dataset obtained through 
             electronic bins. In addition, it is possible plotting the results using a bar plot, box plot, and sociogram. 
	"""
	
	cran = "socialh" 

	version("0.1.1", md5="12aa1b1b308d59a83b65f2af974aaa7f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
