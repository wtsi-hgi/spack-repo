# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopgenreport(RPackage):
	"""A Simple Framework to Analyse Population and Landscape Genetic
Data

	Provides beginner friendly framework to analyse population genetic
    data. Based on 'adegenet' objects it uses 'knitr' to create comprehensive reports on spatial genetic data. 
    For detailed information how to use the package refer to the comprehensive
    tutorials or visit <http://www.popgenreport.org/>.
	"""
	
	homepage = "https://github.com/green-striped-gecko/PopGenReport"
	cran = "PopGenReport" 

	version("3.1", md5="7b17b5e2a8a5bda48ca5ac8986d93380")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-adegenet@2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rgooglemaps", type=("build", "run"))
	depends_on("r-gap", type=("build", "run"))
	depends_on("r-calibrate", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dismo", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-pegas", type=("build", "run"))
	depends_on("r-genetics", type=("build", "run"))
	depends_on("r-gdistance", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-mmod", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
