# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShortform(RPackage):
	"""Automatic Short Form Creation

	Performs automatic creation of short forms of scales with an 
    ant colony optimization algorithm and a Tabu search. As implemented in the 
    package, the ant colony algorithm randomly selects items to build a model of 
    a specified length, then updates the probability of item selection according 
    to the fit of the best model within each set of searches. The algorithm 
    continues until the same items are selected by multiple ants a given number 
    of times in a row. On the other hand, the Tabu search changes one parameter at
    a time to be either free, constrained, or fixed while keeping track of the
    changes made and putting changes that result in worse fit in a "tabu" list
    so that the algorithm does not revisit them for some number of searches. 
    See Leite, Huang, & Marcoulides (2008) <doi:10.1080/00273170802285743> for
    an applied example of the ant colony algorithm, and Marcoulides & Falk (2018)
    <doi:10.1080/10705511.2017.1409074> for an applied example of the Tabu search.
	"""
	
	homepage = "https://github.com/AnthonyRaborn/ShortForm"
	cran = "ShortForm" 

	version("0.5.3", md5="8a6408b46923f43503720a86acd2df57")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lavaan@0.5.22:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
