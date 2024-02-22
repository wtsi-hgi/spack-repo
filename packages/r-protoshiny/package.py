# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProtoshiny(RPackage):
	"""Interactive Dendrograms for Visualizing Hierarchical Clusters
with Prototypes

	Shiny app to interactively visualize hierarchical clustering with prototypes. 
    For details on hierarchical clustering with prototypes, see 
    Bien and Tibshirani (2011) <doi:10.1198/jasa.2011.tm10183>. This package currently launches the application.
	"""
	
	cran = "protoshiny" 

	version("0.1.0", md5="57d87161dbc9b2e75d00a30edc3f8d52")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-protoclust", type=("build", "run"))
	depends_on("r-rare", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
