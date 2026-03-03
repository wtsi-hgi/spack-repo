# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKgschart(RPackage):
	"""KGS Rank Graph Parser

	Restore underlining numeric data from rating history graph of 
    KGS (an online platform of the game of go, <http://www.gokgs.com/>). 
    A shiny application is also provided.
	"""
	
	homepage = "https://github.com/kota7/kgschart"
	cran = "kgschart" 

	version("1.3.5", md5="bd5218825e28ec5d4315dfa035c814ae")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-deepnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
