# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCofra(RPackage):
	"""Complete Functional Regulation Analysis

	Calculates complete functional regulation analysis and visualize
    the results in a single heatmap. The provided example data is for biological
    data but the methodology can be used for large data sets to compare quantitative
    entities that can be grouped. For example, a store might divide entities into
    cloth, food, car products etc and want to see how sales changes in the groups
    after some event. The theoretical background for the calculations are provided
    in New insights into functional regulation in MS-based drug profiling, Ana Sofia
    Carvalho, Henrik Molina & Rune Matthiesen, Scientific Reports <doi:10.1038/srep18826>.
	"""
	
	cran = "CoFRA" 

	version("0.1002", md5="88f353dd3e02de095c0b624c215ada0c")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
