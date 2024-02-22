# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustransition(RPackage):
	"""Monitor Changes in Cluster Solutions of Dynamic Datasets

	Monitor and trace changes in clustering solutions of accumulating datasets 
    at successive time points. The clusters can adopt External and Internal transition at 
    succeeding time points. The External transitions comprise of Survived, Merged, Split, 
    Disappeared, and newly Emerged candidates. In contrast, Internal transition includes changes 
    in location and cohesion of the survived clusters. The package uses MONIC framework developed by 
    Spiliopoulou, Ntoutsi, Theodoridis, and Schult (2006)<doi:10.1145/1150402.1150491> .
	"""
	
	cran = "clusTransition" 

	version("1.0", md5="5c588435c2cc9d9d20f16d13a0494d8d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-flexclust", type=("build", "run"))
