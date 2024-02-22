# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChessboard(RPackage):
	"""Create Network Connections Based on Chess Moves

	Provides functions to work with directed (asymmetric) and 
    undirected (symmetric) spatial networks. It makes the creation of 
    connectivity matrices easier, i.e. a binary matrix of dimension n x n, where 
    n is the number of nodes (sampling units) indicating the presence (1) or  
    the absence (0) of an edge (link) between pairs of nodes. Different network
    objects can be produced by 'chessboard': node list, neighbor list, edge 
    list, connectivity matrix. It can also produce objects that will be used 
    later in Moran's Eigenvector Maps (Dray et al. (2006) <doi:10.1016/j.ecolmodel.2006.02.015>)
    and Asymetric Eigenvector Maps (Blanchet et al. (2008) <doi:10.1016/j.ecolmodel.2008.04.001>), 
    methods available in the package 'adespatial' (Dray et al. (2023) 
    <https://CRAN.R-project.org/package=adespatial>). This work is part of the 
    FRB-CESAB working group Bridge 
    <https://www.fondationbiodiversite.fr/en/the-frb-in-action/programs-and-projects/le-cesab/bridge/>.
	"""
	
	homepage = "https://github.com/frbcesab/chessboard"
	cran = "chessboard" 

	version("0.1", md5="1f037c12af891c40c2ffc0cb0c4e68e1")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
