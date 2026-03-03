# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMobirep(RPackage):
	"""Models Bivariate Dependence and Produces Bivariate Return
Periods

	Models the dependence between two variables in the extremes, identifies most 
    relevant models among six models: the conditional extremes model, the Jt-KDE model 
    and four copulae (Gumbel, Galambos, Normal, FGM). Bivariate return periods for 
    the six models and bivariate level curves can be created.
    Methods used in the package are described in the following reference:
    Tilloy, Malamud, Winter and Joly-Laugel (2020) <doi:10.5194/nhess-20-2091-2020>
    Supporting references for the conditional extremes model,
    Jt-KDE model and for copula modelling are the following: 
    Heffernan and Tawn (2004) <doi:10.1111/j.1467-9868.2004.02050.x>
    Cooley, Thibaud, Castillo and Wehner (2019) <doi:10.1007/s10687-019-00348-0>
    Nelsen (2006) <doi:10.1007/0-387-28678-0>.
	"""
	
	cran = "mobirep" 

	version("0.2.3", md5="39e8d0b12ad166e3eaf716fe42f2dd1d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-texmex", type=("build", "run"))
	depends_on("r-copbasic", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-spatialextremes", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
