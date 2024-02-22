# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreespace(RPackage):
	"""Statistical Exploration of Landscapes of Phylogenetic Trees

	Tools for the exploration of distributions of phylogenetic trees.
    This package includes a 'shiny' interface which can be started from R using
    treespaceServer(). 
    For further details see Jombart et al. (2017) <DOI:10.1111/1755-0998.12676>.
	"""
	
	homepage = "https://cran.r-project.org/package=treespace"
	cran = "treespace" 

	version("1.1.4.3", md5="24c1463ef7661d4d0bba6107bce80f1b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-adegenet", type=("build", "run"))
	depends_on("r-adegraphics", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-distory", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rlumshiny", type=("build", "run"))
	depends_on("r-scatterd3", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
