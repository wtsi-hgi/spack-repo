# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcocopula(RPackage):
	"""Graphical Modelling and Ordination using Copulas

	Creates 'graphs' of species associations (interactions) and ordination biplots from 
    co-occurrence data by fitting discrete gaussian copula graphical models. Methods described in
    Popovic, GC., Hui, FKC., Warton, DI., (2018) <doi:10.1016/j.jmva.2017.12.002>.
	"""
	
	cran = "ecoCopula" 

	version("1.0.2", md5="575012c6205ca194826e775a9060abbb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvabund@4.2:", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tweedie", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
	depends_on("r-ordinal", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
